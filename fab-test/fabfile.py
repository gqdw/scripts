from fabric.api import *

env.user = 'root'
env.hosts = ['123.56.229.114']

def test1():
	run('ls -l /tmp')
