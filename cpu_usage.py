#!/usr/bin/env python3

#practice program to check cpu usage
import psutil

#define function to check CPU usage
def check_cpu_usage(percent):
  usage = psutil.cpu_percent(1)
  print("DEBUG: usage: {}".format(usage))
  return usage < percent

if not check_cpu_usage(75):
  print("ERROR! CPU is overloaded")
else:
  print("Everything is okay!")
