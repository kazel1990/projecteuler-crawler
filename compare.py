import json
import os
PATH='/path/to/'

def compare():
	rlst = os.listdir(PATH+'result/')
	dlst = os.listdir(PATH+'data/')
	fout = open(PATH+'comp', 'w')
	for r in rlst:
		if r in dlst:
			fr = open(PATH+'result/' + r, 'r')
			fd = open(PATH+'data/' + r, 'r')
			lr = json.load(fr)
			ld = json.load(fd)
			fr.close()
			fd.close()
			for n in lr:
				if n not in ld:
					name = r[0] + "_" + r[1:]
					s = '[alarm] ' + name + ' has solved problem ' + str(n)
					fout.write(s+'\n')
	fout.close()

if __name__ == '__main__':
	compare()

