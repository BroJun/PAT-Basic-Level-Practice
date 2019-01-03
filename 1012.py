list_str = input().split()
N = int(list_str[0])
NumList = map(int,list_str[1:])
logiclist = [False]*5
A=[0]*5
pm_A2=1;num_A4=0
for i in NumList:
	mod_of_i = i%5
	if mod_of_i==0 and i%2 == 0:A[1-1] += i;logiclist[0] = True
	if mod_of_i==1:A[2-1] += i*pm_A2;logiclist[1] = True;pm_A2 *= -1
	if mod_of_i==2:A[3-1] += 1;logiclist[2] = True
	if mod_of_i==3:A[4-1] += i;logiclist[3] = True;num_A4+=1
	if mod_of_i==4:
		if i>A[5-1]:A[5-1] = i;logiclist[4] = True
if logiclist[3]:A[4-1] = round(A[4-1]/num_A4,1)
print_str = ['N']*5
for i in range(5):
	if logiclist[i]:print_str[i]=A[i]
i=0
for x in print_str:
	i+=1
	if i==len(print_str):print(x)
	else:print(x,end=" ")
