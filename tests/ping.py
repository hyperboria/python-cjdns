#!/usr/bin/env python
import cjdnsadmin

cjdns = cjdnsadmin.connectWithAdminInfo()
cjdns.ping()
