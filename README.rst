===============================
 python-cjdns For Python 2 & 3
===============================

.. image:: https://travis-ci.org/hyperboria/python-cjdns.svg?branch=master
   :alt: Bulid Status
   :target: https://travis-ci.org/hyperboria/python-cjdns

.. image:: https://landscape.io/github/hyperboria/python-cjdns/master/landscape.svg
   :alt: Code Health
   :target: https://landscape.io/github/hyperboria/python-cjdns/master

.. image:: https://img.shields.io/pypi/v/cjdns.svg
   :alt: PyPI
   :target: https://pypi.python.org/pypi/cjdns

The cjdns python library doesn't support python3 and is a PITA to install, due
to it's use of a modified bencode library which is still called "bencode", among
other things, so I'm cleaning it up.

Installation
============

The easiest way to install it is::

    pip install cjdns

But you could also clone it and run::

    python setup.py install

Once it's installed, you'll find ``peerStats`` and ``cexec`` installed in your ``$PATH``, and the ``cjdns`` library available for import.


Usage
=====

Usage is simple. First, import:

.. code:: python

    import cjdns

Then, connect to the running cjdns instance. There are two ways to do this. The normal way is to use the ``~/.cjdnsadmin`` file:

.. code:: python

    cjdns = cjdns.connectWithAdminInfo()

Or, if you have the IP, port and password and wish to ignore the ``~/.cjdnsadmin`` file for whatever reason:

.. code:: python

    cjdns = cjdns.connect(ip, port, password)

Once connected, you may call any of the `cjdns admin interface functions <https://github.com/cjdelisle/cjdns/blob/master/admin/README.md#cjdns-functions>`_:

.. code:: python

    peerStats = cjdns.InterfaceController_peerStats()

Finally, there is a helper function that allows one to convert a cjdns public key into an IP address:

.. code:: python

    from cjdns import key_utils
    key_utils.to_ipv6('1rfp3guz4jjhfu4dsu5mrz68f7fyp502wcttq6b78xdrjhd4ru80.k')


License
=======
Same as cjdns, this is a GPLv3 project. Full text of the license is available [here](LICENSE)


Contributing
============

I welcome pull requests, please make sure that everything you contribute is pep8 compliant and works on python 2.6, 2.7, 3.2, 3.3 and 3.4. There are some basic tests in place for these things via Travis, but they're not complete by any means.
