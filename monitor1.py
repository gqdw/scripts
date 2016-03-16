import re
import os
import subprocess
import time
# cmd = "ps axu|grep java|grep -v grep  |awk '{print $3,$4}'"

def do_with_ps(ps):
	user = ps[0]
	pid = ps[1]
	cpu = ps[2]
	mem = ps[3]
	command = ps[-1]
	print user, pid, cpu, mem, command


def main():
	cmd = 'ps axu'
	while True:
		child1 = subprocess.Popen(cmd.split(),stdout=subprocess.PIPE)
		res = child1.communicate()
		# print res[0]
		ps = res[0].split('\n')
		for line in ps:
			if re.search('java', line):
				# print line
				ps = line.split()
				do_with_ps(ps)

		time.sleep(5)

if __name__ == '__main__':
	main()