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


input_str = input().split()
input_str.reverse()
print_list(input_str)
