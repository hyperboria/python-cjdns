#!/usr/bin/env python
"""cjdnsadmin
Allows communication with an instance of cjdns via the admin/RPC port.

Usage:

import cjdnsadmin
cjdns = cjdnsadmin.connectWithAdminInfo()

"""
from .cjdnsadmin import connect, connectWithAdminInfo, PublicToIp6
