from fabric.api import *

env.user = 'root'
env.hosts = ['123.56.229.114']

def test1():
	run('ls -l /tmp')

def test2():
	with cd('/usr/local'):
		run('pwd')
		run('ls -l')
