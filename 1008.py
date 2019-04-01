def print_list(a_list):
    flag = 0
    i = 0
    while i < len(a_list):
        if flag == 0:
            print(a_list[i], end='')
            flag = 1
        else:
            print(' ' + str(a_list[i]), end='')
        i += 1
    return 0


str1 = input().split()
str2 = input().split()
N, M = [int(x) for x in str1]
List_A = [int(x) for x in str2]
for i in range(M):
    temp = List_A.pop()
    List_A.insert(0, temp)
print_list(List_A)
