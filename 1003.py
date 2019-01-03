def YES_or_NO(word_str):
	s_P = [];s_A = [];s_T = []
	for i in range(len(word_str)):
		if word_str[i] == 'P':s_P.append(i)
		if word_str[i] == 'A':s_A.append(i)
		if word_str[i] == 'T':s_T.append(i)
	if not (len(s_P) == 1 and len(s_T) == 1 and len(s_A)+2 == len(word_str)):return 'NO'
	if not s_P[0]+1 < s_T[0]:return 'NO'
	if not s_P[0]*(s_T[0]-s_P[0]-1)==(len(word_str)-s_T[0]-1):return 'NO'
	return 'YES'
	
n = int(input())
i=1
input_str=[]
while i<n+1:
	input_str.append(input())
	i += 1

for word_str in input_str:
	print(YES_or_NO(word_str))
