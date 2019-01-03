word1,str1,word2,str2=[x for x in input().split()[:4]]
x=y=0
for i in word1:
	if i == str1 : x += 1
for i in word2:
	if i == str2 : y += 1
if x == 0 : num1 = 0
else: num1 = int(str1*x)
if y == 0 : num2 = 0
else: num2 = int(str2*y)

print(num1+num2)
