n = input()
a = 0
for i in n:
    a += int(i)
if a % 7 == 4:
    print('Bad')
else:
    print('Good')