#!/usr/bin/python2
# -*- coding: utf-8 -*-
# Stolen from https://gist.github.com/pyropeter/642505 - no license attached
import collections


def bencode(obj):
    if isinstance(obj, int):
        return "i" + str(obj) + "e"

    if isinstance(obj, str):
        return str(len(obj)) + ":" + obj

    if isinstance(obj, list):
        res = "l"
        for elem in obj:
            res += bencode(elem)
        return res + "e"

    if isinstance(obj, dict):
        res = "d"
        for key in sorted(obj.keys()):
            res += bencode(key) + bencode(obj[key])
        return res + "e"

    if isinstance(obj, collections.OrderedDict):
        return bencode(dict(obj))
    raise Exception("Unknown object: %s" % repr(obj))


def bdecode(text):
    text = text.decode('utf-8')

    def bdecode_next(start):
        if text[start] == 'i':
            end = text.find('e', start)
            return int(text[start+1:end], 10), end + 1

        if text[start] == 'l':
            res = []
            start += 1
            while text[start] != 'e':
                elem, start = bdecode_next(start)
                res.append(elem)
            return res, start + 1

        if text[start] == 'd':
            res = {}
            start += 1
            while text[start] != 'e':
                key, start = bdecode_next(start)
                value, start = bdecode_next(start)
                res[key] = value
            return res, start + 1

        lenend = text.find(':', start)
        length = int(text[start:lenend], 10)
        end = lenend + length + 1
        return text[lenend+1:end], end
    return bdecode_next(0)[0]

# assert bdecode("i42e") == 42
# assert bdecode("3:foo") == 'foo'
# assert bdecode("li42ei1337ee") == [42, 1337]
# assert bdecode("li42eli42e3:baree") == [42, [42, 'bar']]
# assert bdecode("d3:fooli42eee") == {'foo': [42]}
# assert "i42e" == bencode(42)
# assert "3:foo" == bencode('foo')
# assert "li42ei1337ee" == bencode([42, 1337])
# assert "li42eli42e3:baree" == bencode([42, [42, 'bar']])
# assert "d3:fooli42eee" == bencode({'foo': [42]})

if __name__ == '__main__':
    import sys
    import getopt
    optlist, args = getopt.getopt(sys.argv[1:], 'de')

    if ('-e', '') in optlist:
        from tempfile import NamedTemporaryFile
        import pprint
        import os

        if not len(args):
            raise Exception("No file name given")
        inoutfile = open(args[0], "r")

        tmpfile = NamedTemporaryFile('w', delete=False)

        content = bdecode(inoutfile.read())
        pprint.pprint(content, tmpfile, 2)
        tmpfile.write('\n')
        tmpfile.close()
        inoutfile.close()

        os.system("vim %s" % (tmpfile.name))

        content = eval(open(tmpfile.name).read())
        inoutfile = open(args[0], "w")
        inoutfile.write(bencode(content))
        inoutfile.close()

        os.remove(tmpfile.name)
    else:
        if len(args) and args[0] != '-':
            filehandle = open(args[0], "r")
        else:
            filehandle = sys.stdin

        if ('-d', '') in optlist:
            import pprint
            content = bdecode(filehandle.read())
            pprint.PrettyPrinter(indent=2).pprint(content)
        else:
            content = eval(filehandle.read())
            print(bencode(content))

# vim: set ts=4 sw=4 et:
