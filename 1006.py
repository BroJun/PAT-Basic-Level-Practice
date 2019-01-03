def chai(n):
	n_G = n%10
	n = n//10
	n_S = n%10
	n = n//10	
	n_B = n%10
	n = n//10
	return n_B,n_S,n_G

def G_num(n):
	if n == 0:return None
	G = 0
	for i in range(1,n+1):
		G=G*10+i
	return G

num = int(input())
n_B,n_S,n_G = chai(num)
str_G = str(G_num(n_G))
if str_G == 'None':str_G=''
print('B'*n_B+'S'*n_S+str_G)

