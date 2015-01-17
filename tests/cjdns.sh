#!/bin/bash
echo "Installing cjdns..."
git clone https://github.com/cjdelisle/cjdns
cd cjdns
./do

echo "Generating, cleaning conf"
./cjdroute --genconf | ./cjdroute --cleanconf > ~/cjdroute.conf
python2 contrib/python/cjdnsadminmaker.py
/opt/cjdns/contrib/nodejs/tools/cexec.js 'ping()'
