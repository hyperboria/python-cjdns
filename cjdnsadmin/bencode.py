#!/usr/bin/python
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

    if isinstance(obj, unicode):
        return bencode(obj.encode('utf-8'))

    if isinstance(obj, collections.OrderedDict):
        return bencode(dict(obj))
    raise Exception("Unknown object: %s (%s)" % (repr(obj), repr(type(obj))))


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

# vim: set ts=4 sw=4 et:
