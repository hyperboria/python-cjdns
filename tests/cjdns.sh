#!/bin/bash
echo "Installing cjdns..."
git clone https://github.com/cjdelisle/cjdns
cd cjdns
./do

echo "Generating, cleaning conf"
./cjdroute --genconf | ./cjdroute --cleanconf > ~/cjdroute.conf
./cjdroute < ~/cjdroute.conf
python2 contrib/python/cjdnsadminmaker.py
contrib/nodejs/tools/cexec.js 'ping()'
