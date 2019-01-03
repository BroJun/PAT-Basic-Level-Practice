num = [int(x) for x in input().split()[:10]]
strnum=''
for x in ['0','1','2','3','4','5','6','7','8','9']:
	strnum = strnum + x * num[int(x)]
strnum = list(strnum)
i = 1
while True:
	if strnum[0] != '0' : break
	temp = strnum.pop(i)
	strnum.insert(0,temp)
	i += 1
strnum = ''.join(strnum)
print(strnum)
