def FirstDateIsAfter(FirstDate, SecondDate):
    FDT = FirstDate.split('/')
    SDT = SecondDate.split('/')
    '''
	FD = [int(x) for x in FDT]
	SD = [int(x) for x in SDT]
	'''
    FD = list(map(int, FDT))
    SD = list(map(int, SDT))

    if FD[0] > SD[0]:
        return True
    elif FD[0] == SD[0]:
        if FD[1] > SD[1]:
            return True
        elif FD[1] == SD[1]:
            if FD[2] > SD[2]:
                return True
    else:
        return False


def IsValid(ADate):
    EarliestDate = '1814/09/05'
    LatestDate = '2014/09/07'
    if FirstDateIsAfter(ADate, EarliestDate) and FirstDateIsAfter(LatestDate, ADate):
        return True
    else:
        return False


N = int(input())
names = []
dates = []
for i in range(N):
    tempstr = input().split()
    names.append(tempstr[0])
    dates.append(tempstr[1])

nValid = 0
firstValid = -1

i = 0
for x in dates:
    if IsValid(x):
        firstValid = i
        nValid += 1
        break
    else:
        i += 1
'''
while True:
	if IsValid(dates[firstValid]):
		nValid += 1
		break
	else:
		firstValid += 1
'''
if firstValid == -1:
    print('0')
else:
    nnOldman = firstValid
    nnYoungman = firstValid
    if firstValid + 1 < N:
        for i in range(firstValid + 1, N):
            if not IsValid(dates[i]):
                continue
            else:
                nValid += 1
                if FirstDateIsAfter(dates[nnOldman], dates[i]):
                    nnOldman = i
                if FirstDateIsAfter(dates[i], dates[nnYoungman]):
                    nnYoungman = i
    print(nValid, names[nnOldman], names[nnYoungman])

    # print(FirstDateIsAfter('1814/09/06','2014/09/06'))
