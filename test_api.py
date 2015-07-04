import ansible.runner

import json

runner = ansible.runner.Runner(
	module_name='ping',
	module_args='',
	pattern='test',
	remote_user='root',
	
	forks=10)

data = runner.run()
res = json.dumps(data)
print data
