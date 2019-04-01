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


def fun(temp, list_n):
    if temp == 0:
        return list_n
    list_n.append(temp % 10)
    temp = temp // 10
    return fun(temp, list_n)


def get_list(n):
    list_n = []
    list_n = fun(n, list_n)
    list_n.reverse()
    return list_n


def get_str(list_of_sum):
    list_str = []
    for x in list_of_sum:
        if x == 1:
            list_str.append('yi')
        elif x == 2:
            list_str.append('er')
        elif x == 3:
            list_str.append('san')
        elif x == 4:
            list_str.append('si')
        elif x == 5:
            list_str.append('wu')
        elif x == 6:
            list_str.append('liu')
        elif x == 7:
            list_str.append('qi')
        elif x == 8:
            list_str.append('ba')
        elif x == 9:
            list_str.append('jiu')
        elif x == 0:
            list_str.append('ling')
    return list_str


def main():
    n = int(input())
    list_n = get_list(n)
    sum_of_list_n = sum(list_n)
    list_of_sum = get_list(sum_of_list_n)
    list_str = get_str(list_of_sum)
    print_list(list_str)


main()
