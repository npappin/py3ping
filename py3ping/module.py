#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Stuff
RETURN CODES
  10 =
"""

import os, socket

class Statistics:
  destination = ""

def pyPing(host, count=1, size=100, verbose=False):
  """
  Do a ping.
  """
  try:
    ip = socket.gethostbyname(host)
  except Exception as e: raise e
  if count != abs(count): raise ValueError
  print(ip)
  print(count)
  for i in range(count):
    sendPing(host)
    receivePing()

def systemPing(host, verbose=False):
  if verbose==True: return(os.system("ping -c 1 {}".format(host)))
  else: return(os.system("ping -c 1 {} >> /dev/null".format(host)))

def ping(host, count=1):
  output=os.system("fping -c{} -s {}".format(count, host))
  pass

def sendPing(host):
  """
  Send a single ping.
  """
  print("sendPing")
  return

def receivePing(socket=None):
  """
  Receive a single ping.
  """
  print("receivePing")
  return
