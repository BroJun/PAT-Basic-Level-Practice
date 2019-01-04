def m2e(words):
	ge = ['tret','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec' , 'tam']
	shi = ['tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']
	if len(words) == 1:
		return ge.index(words[0])
	else:
		shiwei = shi.index(words[0]) + 1
		gewei = ge.index(words[1])
		return shiwei * 13 + gewei

def e2m(n):
	
	ge = ['tret','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec' , 'tam']
	shi = ['tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']
	shiwei = n // 13
	gewei = n % 13
	if shiwei == 0 : return ge[gewei]
	else:
		return shi[shiwei-1]+' '+ge[gewei]

ge = ['tret','jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec' , 'tam']

N = int(input())

for i in range(N):
	words = []
	for x in input().split():
		words.append(x)
	
	if words[-1] in ge:
		print(m2e(words))
	else:
		words = int(words[0])
		print(e2m(words))
	
