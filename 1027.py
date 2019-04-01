'''
def use(n):
	if n == 0 : return 0
	sum_n = 1
	for i in range(1,n):
		sum_n += 4*i + 2
	return sum_n

num , a_str= input().split()[:2]
num = int(num)
a_str = a_str[:1]

def main():
	if num == 0 : return 0
	i = 0
	while True:
		if use(i) <= num and use(i+1)>num : break
		i+=1
	
	max_num = 2 * i - 1
	for j in range(i,0,-1):
		this_num = 2 * j - 1
		space_num = (max_num - this_num) // 2
		print(' '*space_num + a_str * this_num)
	for j in range(2,i+1,1):
		this_num = 2 * j - 1
		space_num = (max_num - this_num) // 2
		print(' '*space_num + a_str * this_num)
	least_num = num - use(i)
	if least_num != 0 : print(least_num)

main()
'''


def use(n):
    if n == 0:
        return 0
    sum_n = 1
    for i in range(1, n):
        sum_n += 4 * i + 2
    return sum_n


num, a_str = input().split()[:2]
num = int(num)
a_str = a_str[:1]

i = 0
while True:
    if use(i) <= num and use(i + 1) > num:
        break
    i += 1

max_num = 2 * i - 1
for j in range(i, 0, -1):
    this_num = 2 * j - 1
    space_num = (max_num - this_num) // 2
    print(' ' * space_num + a_str * this_num)
for j in range(2, i + 1, 1):
    this_num = 2 * j - 1
    space_num = (max_num - this_num) // 2
    print(' ' * space_num + a_str * this_num)
least_num = num - use(i)
'''
if least_num != 0 : 
	print(least_num)
'''
print(least_num)
