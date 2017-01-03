#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Stuff
"""

import os, socket

def ping(host):
  """
  Stuff to do a ping
  """
  ip = socket.gethostbyname(host)
  print(ip)
