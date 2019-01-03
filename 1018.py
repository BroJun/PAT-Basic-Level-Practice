
num = int(input())

list_1=[]
list_2=[]

for i in range(num):
	str1,str2=[x for x in input().split()[:2]] 
	list_1.append(str1)
	list_2.append(str2)          

wins , draws , losses = 0 , 0 , 0
jia_C = jia_J = jia_B = yi_C =  yi_J = yi_B = 0

for i in range(num):
	if list_1[i] == list_2[i] : draws += 1
	elif (list_1[i] == 'C' and list_2[i] == 'J'): wins += 1;jia_C +=1
	elif (list_1[i] == 'J' and list_2[i] == 'B'): wins += 1;jia_J +=1
	elif (list_1[i] == 'B' and list_2[i] == 'C'): wins += 1;jia_B +=1 
	elif (list_1[i] == 'J' and list_2[i] == 'C'): losses += 1;yi_C +=1
	elif (list_1[i] == 'B' and list_2[i] == 'J'): losses += 1;yi_J +=1
	elif (list_1[i] == 'C' and list_2[i] == 'B'): losses += 1;yi_B +=1 

if jia_B>=jia_C and jia_B>=jia_J: best_jia = 'B'
elif jia_C>=jia_B and jia_C>=jia_J: best_jia = 'C'
else: best_jia = 'J'

if yi_B>=yi_C and yi_B>=yi_J: best_yi = 'B'
elif yi_C>=yi_B and yi_C>=yi_J: best_yi = 'C'
else: best_yi = 'J'

print(wins , draws , losses)
print(losses , draws , wins)
print(best_jia , best_yi)
