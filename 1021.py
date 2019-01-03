N = input()
sum_N = [0]*10
for x in N:
	for y in ['0','1','2','3','4','5','6','7','8','9']:
		if y == x : sum_N[int(y)] += 1
for i in range(10):
	if sum_N[i] != 0 : print(str(i)+':'+str(sum_N[i]))
	else : continue
		

	
