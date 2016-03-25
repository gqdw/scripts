import json
from collections import Counter

lt = []
# with open('/Users/gqdw/test.txt') as f:
with open('/Users/gqdw/namebug.txt') as f:
	for i in f:
		# print i
		var = json.loads(i)
		lt.append(var['Authorization:Bearer'])

cnt = Counter(lt)
print cnt.most_common(10)

