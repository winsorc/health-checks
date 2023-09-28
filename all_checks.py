#!/usr/bin/env python3
import shutil
import os
import sys
import psutil

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

def main():
  if check_reboot():
    print("Pending Reboot.")
    sys.exit(1)
  if check_root_full():
    print("Root partition full.")
    sys.exit(1)

  print("Everything is ok.")
  sys.exit(0)

main()

