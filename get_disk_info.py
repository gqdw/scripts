import subprocess

def myrun(cmd):
	return subprocess.Popen(cmd.split(), stdout=subprocess.PIPE).communicate()[0]

out1 = myrun('ls /tmp')
print out1
output = subprocess.Popen(["df"], stdout=subprocess.PIPE).communicate()[0]
print output
if 'data' in output.split():
	disk1 = [i for i in output.split('\n') if 'data' in i][0].split()[4]
	print disk1
else:
	print 'these is not data disk'

