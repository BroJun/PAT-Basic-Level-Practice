
# A,B = [int(x) for x in input().split()[:2]]

A, B = map(int, input().split()[:2])

Q = A // B
R = A % B
print(Q, R)
