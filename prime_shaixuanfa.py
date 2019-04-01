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
    start = time.process_time()
    n = 10000000
    P = primes(n)
    print("There are %d primes less than %d" % (len(P), n))
    # for i in range(10):
    #  print(P[i])
    print("Time: %f" % (time.process_time() - start))
    # for n in range(2,100000):
    #  if isPrime(n):
    #    print("%d is prime"%n)
    # print("%d is "%n + ("prime" if isPrime(n) else "not prime"))

    start = time.process_time()
    n = 1000000
    print("There are %d primes less than %d" % (primeCnt(n), n))
    print("Time: %f" % (time.process_time() - start))
