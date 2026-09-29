n = int(input())
c = 0
for i in range(n):
    s = input()
    if len(s) <= 3 or 'tap' in s or 'xocure' in s:
        print(s)
        c += 1
if c <= 3:
    print('safe')
elif c <= 6:
    print('warning')
else:
    print('danger')