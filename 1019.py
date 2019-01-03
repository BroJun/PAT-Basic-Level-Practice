def num2str(num):
	if num >= 1000 : return str(num)
	elif num >= 100: return '0' + str(num)
	elif num >= 10 : return '00'+ str(num)
	elif num >= 0 :return '000' + str(num)
	else: return 'xxxx'

num_str = input()

if len(num_str)==4 and sorted(num_str) == sorted(num_str,reverse=True):
	
	print(num_str+' - '+num_str+' = 0000')
else:
	while True:
		num1 = int(''.join(sorted(num_str,reverse = True)))
		if 100 <= num1 < 1000 : num1 = num1 * 10
		elif 10 <= num1 < 100 : num1 = num1 * 100
		elif 1 <= num1 < 10 : num1 = num1 * 1000
		num2 = int(''.join(sorted(num_str,reverse = False)))
		num3 = num1 - num2
		
		print(num2str(num1)+' - '+num2str(num2)+' = '+num2str(num3))
		
		if num3 == 6174 : break
		num_str = str(num3)
