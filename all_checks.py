#!/usr/bin/env python3
import shutil
import os
import sys
import psutil

def check_reboot():
  #Returns True if the computer has pending reboot.
  return os.path.exists("/run/reboot-required")

def check_disk_usage(disk, min_absolute, min_percent):
  #returns true if there is enough free space, false if not
  du = shutil.disk_usage(disk)
  #calculate percentage of free space
  percent_free = 100 * du.free / du.total
  #calculate how many free gigabytes
  gigabytes_free = du.free /2**30
  if percent_free < min_percent or gigabytes_free < min_absolute:
    return False
  return True
if not check_disk_usage("/", 2, 10):
  print("ERROR: Not enough disk space.")
  sys.exit(1)

print("Enough disk space")

def check_cpu_usage(percent):
  usage = psutil.cpu_percent(1)
  print("CPU usage %: {}".format(usage))
  return usage < percent

if not check_cpu_usage(75):
  print("ERROR! CPU is overloaded")
else:
  print("CPU  is okay!")

def main():
  if check_reboot():
    print("Pending Reboot.")
    sys.exit(1)
  print("No reboot pending.")
  sys.exit(0)

main()
check_disk_usage()
check_cpu_usage()
