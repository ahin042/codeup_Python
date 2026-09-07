a = input()
b = [] ; n = len(a)
m = 1 ; r = 0 ; v = True
for i in range(n):
    c = a[i]
    if c == '(':
        b.append('(')
        m *= 2
    elif c == '[':
        b.append('[')
        m *= 3
    elif c == ')':
        if not b or b[-1] != '(':
            v = False
            break
        if a[i-1] == '(':
            r += m
        b.pop()
        m //= 2
    elif c == ']':
        if not b or b[-1] != '[':
            v = False
            break
        if a[i-1] == '[':
            r += m
        b.pop()
        m //= 3
if b:
    v = False
print(r if v else 0)