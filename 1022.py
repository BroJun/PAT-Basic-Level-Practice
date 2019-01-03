def zhuan(AB,D):
	result = ''
	while True:
		shang = AB // D
		yu = AB % D
		result = result + str(yu)
		if shang == 0 : break
		else : AB = shang
	return int(result[::-1])
A , B , D = [int(x) for x in input().split()[:3]]
AB = A + B
print(zhuan(AB,D))
