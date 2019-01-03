N = int(input())
i = 0
while N > 1:
  if N%2 == 0:
    N = N / 2
  else:
    N = (3*N+1)/2
  i += 1
print(i)
