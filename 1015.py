class Student:
    def __init__(self, number, score_de, score_cai):
        self.number = number
        self.score_de = score_de
        self.score_cai = score_cai

    def isgood(self, L, H):
        if self.score_de >= L and self.score_cai >= L:
            return True
        return False

    def decide_class(self, L, H):
        if not self.isgood(L, H):
            return 'class0'
        if self.score_de >= H and self.score_cai >= H:
            return 'class1'
        if self.score_de >= H and self.score_cai < H:
            return 'class2'
        if H > self.score_de >= self.score_cai:
            return 'class3'
        return 'class4'


input_str = input().split()
N, L, H = [int(x) for x in input_str[:3]]
all_student = []
for i in range(N):
    input_str = input().split()
    number, score_de, score_cai = [int(x) for x in input_str[:3]]
    all_student.append(Student(number, score_de, score_cai))

list_1 = []
list_2 = []
list_3 = []
list_4 = []

for x in all_student:
    decided_class = x.decide_class(L, H)
    if decided_class == 'class1':
        list_1.append(x)
    elif decided_class == 'class2':
        list_2.append(x)
    elif decided_class == 'class3':
        list_3.append(x)
    elif decided_class == 'class4':
        list_4.append(x)
'''
    if x.isgood(L,H) == False : continue
    else:
      decided_class = x.decide_class(L,H)
      if decided_class == 'class1': list_1.append(x)
      elif decided_class == 'class2' : list_2.append(x)
      elif decided_class == 'class3' : list_3.append(x)
      elif decided_class == 'class4' : list_4.append(x)
'''

list_1.sort(key=lambda student: (student.score_de + student.score_cai,
                                 student.score_de, -student.number), reverse=True)
list_2.sort(key=lambda student: (student.score_de + student.score_cai,
                                 student.score_de, -student.number), reverse=True)
list_3.sort(key=lambda student: (student.score_de + student.score_cai,
                                 student.score_de, -student.number), reverse=True)
list_4.sort(key=lambda student: (student.score_de + student.score_cai,
                                 student.score_de, -student.number), reverse=True)

total_list = list_1 + list_2 + list_3 + list_4
print(len(total_list))
for x in total_list:
    print(str(x.number) + ' ' + str(x.score_de) + ' ' + str(x.score_cai))
