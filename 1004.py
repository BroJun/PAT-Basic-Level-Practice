n = int(input())
i = 1
name_list = []
num_list = []
score_list = []
max_score = -1
min_score = 101
max_num = -1
min_num = -1
while i < n + 1:
    input_str = input()
    list_str = input_str.split()
    name_list.append(list_str[0])
    num_list.append(list_str[1])
    score_list.append(int(list_str[2]))

    if score_list[-1] > max_score:
        max_score = score_list[-1]
        max_num = i
    if score_list[-1] < min_score:
        min_score = score_list[-1]
        min_num = i

    i += 1

print(name_list[max_num - 1] + ' ' + num_list[max_num - 1])
print(name_list[min_num - 1] + ' ' + num_list[min_num - 1])
