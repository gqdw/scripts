with  open('t.txt')  as f:
	with  open('out.txt','w') as fw:
		for line in f.readlines():	
			(l1,l2) = line.split()
			print l1,l2
			fw.write(l1 + ':\n')
			fw.write('  host: ' + l2 + '\n')
			fw.write('  user: user01\n')
			fw.write('  password: P@ssword01!..\n')
			fw.write('  sudo: True\n')
