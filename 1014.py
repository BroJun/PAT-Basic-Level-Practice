list_day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
# d = {:,:,:,:,:,:,:,:,:,:}
str_day1 = input()
str_day2 = input()
str_time1 = input()
str_time2 = input()

i = 0
while True:
	if str_day1[i] == str_day2[i] and 'A'<=str_day1[i]<='G':break
	i += 1
key1 = str_day1[i]

i += 1
while True:
	if str_day1[i] == str_day2[i] and ('0'<=str_day1[i]<='9' or 'A'<=str_day1[i]<='N'):break
	i += 1
key2 = str_day1[i]

i = 0
while True:
	if str_time1[i] == str_time2[i] and ('a'<=str_time1[i]<='z' or 'A'<=str_time1[i]<='Z'):break
	i += 1
key3 = i

s1 = list_day[ord(key1) - 64 -1]

s2 = ord(key2)-55
if s2 < 10 : s2 = s2 + 7

s2 = str(s2)
if len(s2) == 1: s2 = '0' + s2

s3 = str(key3)
if len(s3) == 1: s3 = '0' + s3

print(s1+' '+s2+':'+s3)


