
def print_list(a_list):
	flag = 0
	i = 0
	while i < len(a_list):
		if flag == 0:
			print(a_list[i],end = '')
			flag = 1
		else:
			print(' %d' % a_list[i],end = '')
		i += 1
	return 0
	
def Insertion_onestep(a_list):
	p = 0;
	flag = 0;
	while p < len(a_list)-1:
		if a_list[p+1]<a_list[p]:
			flag = 1			
			break
		p += 1
	p += 1	
	if flag == 1:
		temp = a_list[p]
		a_list.pop(p)
		for i in range(0,p):
			if a_list[i]>temp:
				a_list.insert(i,temp)
				break
	return a_list
	
def Merge_onestep(a_list,n):
	nn = 2**n
	lenl = len(a_list)
	i = 0
	while i < lenl - 1:
		itemp = i + nn -1
		if itemp > lenl -1:
			itemp = lenl-1
		a_list[i:itemp+1]=sorted(a_list[i:itemp+1])
		i = itemp + 1
	n=n+1
	return a_list,n

num = input()
str_num = input().split()
list_num = [int(x) for x in str_num]
str_num2 = input().split()
target_num = [int(x) for x in str_num2]

Insertion_list = list_num[:]
Merge_list = list_num[:]
sort_type = ''
n=1
while True:
	Insertion_list=Insertion_onestep(Insertion_list)
	Merge_list,n=Merge_onestep(Merge_list,n)
	if Insertion_list == target_num:
		sort_type = 'Insertion Sort'
		break
	elif Merge_list == target_num:
		sort_type = 'Merge Sort'
		break

if sort_type == 'Insertion Sort':
	next_list = Insertion_onestep(Insertion_list)
elif sort_type == 'Merge Sort':
	next_list,n = Merge_onestep(Merge_list,n)

print(sort_type)
print_list(next_list)
