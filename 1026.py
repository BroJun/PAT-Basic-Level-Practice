def time_str(n):
    if n >= 10:
        return str(n)
    if n < 10:
        return '0' + str(n)


C1, C2 = map(int, input().split()[:2])
CLK_TCK = 100
# time_s = int( '%.0f' % ((C2-C1)/CLK_TCK) )
time_s = int((C2 - C1) / CLK_TCK + 0.5)
# print(time_s)
hour = time_s // 3600
time_s = time_s % 3600
minute = time_s // 60
time_s = time_s % 60
print(time_str(hour) + ':' + time_str(minute) + ':' + time_str(time_s))
