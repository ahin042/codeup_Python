import datetime
a = input().strip()
b = input().strip()
a1, a2, a3 = map(int, a.split('.'))
b1, b2, b3 = map(int, b.split('.'))
m = datetime.date(a1, a2, a3)
n = datetime.date(b1, b2, b3)
r = 0 ; c = 0 ; i = m
while i <= n:
    if i.weekday() == 4:
        r += (i.month + i.day)
        c += (i.month + i.day) * 2
    i += datetime.timedelta(days = 1)
print(r, c)