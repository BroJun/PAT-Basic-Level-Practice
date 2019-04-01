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


def d(a, n):
    if n == 0:
        a = 0
        n = 0
    else:
        a = a * n
        n = n - 1
    return a, n


input_str = input().split()
list_num = [int(x) for x in input_str]

out_list = []
lenl = len(list_num)
for i in range(0, lenl, 2):
    a, n = d(list_num[i], list_num[i + 1])
    if a != 0:
        out_list.extend([a, n])
if out_list == []:
    print('0 0')
else:
    print_list(out_list)
