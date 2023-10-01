#!/usr/bin/env python3
import shutil
import os
import sys
import psutil
import socket

def check_reboot():
  #Returns True if the computer has pending reboot.
  return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):
  #returns true if there is enough free space, false if not
  du = shutil.disk_usage(disk)
  #calculate percentage of free space
  percent_free = 100 * du.free / du.total
  #calculate how many free gigabytes
  gigabytes_free = du.free /2**30
  if gigabytes_free < min_gb or percent_free < min_percent:
    return True
  return False

def check_root_full():
  """Returns True if the root parition is full, False otherwise."""
  return check_disk_full(disk="/", min_gb=2, min_percent=10)

def check_no_network():
  """Returns True if fails to resolve Google URL, False if succeeds"""
  try:
    socket.gethostbyname("www.google.com")
    return False
  except:
    return True

def main():
  checks=[
    (check_reboot, "Pending Reboot"),
    (check_root_full,  "Root partition full"),
    (check_no_network, "Netowrk connection issue.")
  ]

  everything_ok=True
  for check, msg in checks:
    if check():
      print(msg)
      everything_ok= False
  if not everything_ok:
    sys.exit(1)

  print("Everything is okay!")
  sys.exit(0)

  

main()
