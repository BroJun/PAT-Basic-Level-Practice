# solution1
# import math
# def is_prime(number):
# if number > 1:
# if number == 2:
# return True
# if number % 2 == 0:
# return False
# for current in range(3, int(math.sqrt(number) + 1), 2):
# if number % current == 0:
# return False
# return True

# num = int(input())
# count_n = 0
# # logic_num = list(map(is_prime,range(3,num+1,2)))
# # lenl = len(logic_num)
# # for i in range(0,lenl-1):
# # if logic_num[i] and logic_num[i+1]:count_num+=1
# P = [x for x in range(3,num+1,2) if is_prime(x)]
# for i in range(len(P) - 1):
# if P[i+1]-P[i]==2:count_n+=1
# print(count_n)

# solution2
# def easyprm(N):
# a = [0] * (N + 1)
# a[0] = a[1] = 1
# for i in range(2, N // 2 + 1):
# for j in range(2, N // i + 1):
# a[i * j] = 1
# res=[2]
# for i in range(3,N+1,2):
# if a[i]==0:
# res.append(i)
# return res
# N=int(input())
# A=easyprm(N)
# sum=0
# for i in range(len(A)-1):
# if A[i+1]-A[i]==2:
# sum+=1
# print(sum)

# solution3
import time


def primes(n):
    P = []
    f = []
    for i in range(n + 1):
        if i > 2 and i % 2 == 0:
            f.append(1)
        else:
            f.append(0)

    i = 3
    while i * i <= n:
        if f[i] == 0:
            j = i * i
            while j <= n:
                f[j] = 1
                j += i + i
        i += 2

    P.append(2)
    for i in range(3, n, 2):
        if f[i] == 0:
            P.append(i)
    return P


def isPrime(n):
    if n > 2 and n % 2 == 0:
        return 0

    i = 3
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 2

    return 1


def primeCnt(n):
    cnt = 0
    for i in range(2, n):
        if isPrime(i):
            cnt += 1
    return cnt


if __name__ == '__main__':
    num = int(input())
    P = primes(num + 1)
    # print(P)
    count_n = 0
    for i in range(len(P) - 1):
        if P[i + 1] - P[i] == 2:
            count_n += 1
    print(count_n)
