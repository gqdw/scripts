from fabric.api import *

env.user = 'deploy'
env.hosts = ['192.168.100.52']

def test1():
	print "test1"
	output = local('ls -l /tmp', capture=True)
	print "output: -->" + output

def test2():
	with cd('/usr/local'):
		run('pwd')
		run('ls -l')

def deploy():
	local('tar cf dist.tar dist')
	d = local('pwd', capture=True)
	# print type(d)
	filename = "%s/dist.tar" % d
	dirname = "%s/dist" % d
	print filename
	put(filename, filename)
	with cd(d):
		run('rm -rf dist')
		run('tar xf dist.tar')
		run('ls -l')

