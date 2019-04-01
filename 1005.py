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


def three_n(n):
    set_n = set()
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n + 1) // 2
        set_n.add(n)
    return(set_n)


num = input()
str_num = input().split()
list_num = [int(x) for x in str_num]
logic_num = [True for x in str_num]
i = 0
while i < len(list_num):
    if logic_num[i] == True:
        set_n = three_n(list_num[i])
        j = 0
        while j < len(list_num):
            if list_num[j] in set_n:
                logic_num[j] = False
            j += 1
    i += 1

core_list = []
i = 0
while i < len(list_num):
    if logic_num[i] == True:
        core_list.append(list_num[i])
    i += 1

core_list.sort(reverse=True)
print_list(core_list)
