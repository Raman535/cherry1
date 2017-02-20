#!/usr/bin/python
import subprocess
import os
output=subprocess.check_call(['ls -l>output.txt',shell=True])
print("hello raman\n")
