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
# input_str=input().split()
# M,N = map(int,input_str[:2])
# for


def prime(n, result):
    flag = [1] * (n + 2)
    p = 2
    while(p <= n):
        result.append(p)
        for i in range(2 * p, n + 1, p):
            flag[i] = 0
        while 1:
            p += 1
            if(flag[p] == 1):
                break


a = input().split()
result = []
prime(200000, result)
final = result[int(a[0]) - 1:int(a[1])]
if len(final) == 1:
    print(final[0])
else:
    for i in range(len(final) - 1):
        if (i + 1) % 10 == 0:
            print(final[i])
        else:
            print(final[i], end=" ")
    if (i + 2) % 10 == 0:
        print(final[i + 1])
    else:
        print(final[i + 1], end="")
