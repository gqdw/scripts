#!/usr/bin/env python
import subprocess

"""
A ssh based command dispatch system
"""

machines = []
machines.append('123.56.229.114')

cmd = 'uname'

for machine in machines:
	subprocess.call("ssh root@%s %s" % (machine, cmd),shell=True)
