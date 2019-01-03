in_str = input()
n_PATest = [0]*6
for x in in_str:
	if x == 'P': n_PATest[0] += 1
	elif x == 'A': n_PATest[1] += 1
	elif x == 'T': n_PATest[2] += 1
	elif x == 'e': n_PATest[3] += 1
	elif x == 's': n_PATest[4] += 1
	elif x == 't': n_PATest[5] += 1
	flag = [ ( 1 if x > 0 else 0 ) for x in n_PATest]
while True:
	if n_PATest[0] <= 0 and n_PATest[1] <= 0 and n_PATest[2] <= 0 and n_PATest[3] <= 0 and n_PATest[4] <= 0 and n_PATest[5] <= 0 : break
	print('P'*flag[0]+'A'*flag[1]+'T'*flag[2]+'e'*flag[3]+'s'*flag[4]+'t'*flag[5],end = '')
	n_PATest = [ x-1 for x in n_PATest]
	flag = [ ( 1 if x > 0 else 0 ) for x in n_PATest]
	
