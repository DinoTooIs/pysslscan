#!/usr/bin/env python
import sys

if sys.version_info[0] != 2:
    print("[!] This program is only compatible with python 2")
    exit(-1)

from sslscan import ui

ui.run()

