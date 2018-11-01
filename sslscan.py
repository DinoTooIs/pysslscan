#!/usr/bin/env python
import sys

if sys.version_info[0] < 3:
    print("[!] Please use python3 to have multithread support")
    exit(-1)

from sslscan import ui

ui.run()

