pySSLScan
=========

pySSLScan is a framework to scan SSL enabled services, in order to determine
the supported ciphers, preferred ciphers, certificate information and more.
It is designed to be flexible, lean and fast.

It can be used as a library in other software projects and provides a command-line tool to get started.

You can find more information in the `documentation`_.


Features
--------

* Query SSL services
* Supported cryptographic protocols:

  * SSLv2, SSLv3, TLS 1.0, TLS 1.1 and TLS 1.2
  * DTLS 1.0 and DTLS 1.2

* Supported Protocols:

  * TCP, HTTP, IMAP, POP3, SMTP, LDAP and RDP
  * UDP

* IPv4 and IPv6
* Scan modules:

  * Supported ciphers
  * Ciphers preferred
  * Supported compression methods
  * Supported elliptic curves
  * Test support for Signaling Cipher Suite Value (SCSV)
  * Extract EC Point Formats
  * Server certificate (requires pyOpenSSL)
  * Test renegotiation (requires pyOpenSSL)
  * Detect vulnerabilities

    * Heartbleed

  * Extract server information: HTTP, IMAP, POP3 and SMTP

* Rule based result highlighting
* Output formats:

  * text/terminal


Install
-------

Requirements:

* Python 2.7 or Python >= 3.2
* Python packages:

  * requests_SSL_v2
  * flextls >= 0.3
  * six >= 1.4.1

* Python packages(optional):

  * cryptography >= 0.5
  * pyOpenSSL >= 0.14

Install:

.. code-block:: console

   $ pip3 install -r requirements.txt

Usage
-----

To scan a HTTPS service:


.. code-block:: console

    $ python3 sslscan.py --scan=protocol.http --scan=vuln.heartbleed --scan=server.renegotiation \
      --scan=server.preferred_ciphers --scan=server.ciphers \
      --report=term:rating=ssllabs.2009e --ssl2 --ssl3 --tls10 --tls11 --tls12 http://example.org


To display more information:

.. code-block:: console

    $ python3 sslscan.py --help


License
-------

Published under the LGPLv3+ (see LICENSE for more information)

.. _`documentation`: http://pysslscan.readthedocs.org/ 
