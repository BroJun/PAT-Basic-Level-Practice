num = int(input())
A_list = []
B_list = []
C_list = []
for i in range(num):
    input_str = input().split()
    A_list.append(int(input_str[0]))
    B_list.append(int(input_str[1]))
    C_list.append(int(input_str[2]))
for i in range(num):
    if A_list[i] + B_list[i] > C_list[i]:
        str_temp = ': true'
    else:
        str_temp = ': false'
    print('Case #' + str(i + 1) + str_temp)
