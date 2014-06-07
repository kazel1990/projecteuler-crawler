import json
import os

def compare():
	rlst = os.listdir('result/')
	dlst = os.listdir('data/')
	fout = open('comp', 'w')
	for r in rlst:
		if r in dlst:
			fr = open('result/' + r, 'r')
			fd = open('data/' + r, 'r')
			lr = json.load(fr)
			ld = json.load(fd)
			fr.close()
			fd.close()
			for n in lr:
				if n not in ld:
					s = r + ' has solved problem ' + str(n)
					fout.write(s+'\n')
	fout.close()

if __name__ == '__main__':
	compare()

