
x = time.localtime()
month = x[1]
day = x[2]
md = {1:31,2:28,3:31,4:30,5:31,7:31,8:31,10:31,12:31,6:30,9:30,11:30}
today = 22
num = 72
if month == 3:
    num = day - today


if month-3>0:
    k = month-4
    num = 31 - today
    for i in range(k):
        num = num + md[month-1]
    num = num + day
