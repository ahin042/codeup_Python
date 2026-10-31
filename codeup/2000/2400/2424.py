q = int(input())
m = []
p = {}
count = {}
for i in range(q):
    a = input().split()
    n = a[0]
    if n == 'insert':
        name = a[1]
        p = int(a[2])
        c = int(a[3])
        if name not in p:
            m.append(name)
        p[name] = p
        count[name] = c
    elif n == 'total':
        s = 0
        for i in range(len(m)):
            k = m[i]
            s += p[k] * count[k]
        print(s)
    elif n == 'best':
        mx = -1
        ans = ""
        for i in range(len(m)):
            k = m[i]
            val = count[k]
            if val > mx:
                mx = val
                ans = k
        print(ans)
    elif n == 'worst':
        mn = 10 ** 18
        ans = ""
        for i in range(len(m)):
            k = m[i]
            val = count[k]
            if val < mn:
                mn = val
                ans = k
        print(ans)
    elif n == 'countall':
        c = 0
        for i in range(len(m)):
            k = m[i]
            c += count[k]
        print(c)
    elif n == 'totalif':
        x = int(a[1])
        s = 0
        for i in range(len(m)):
            k = m[i]
            if p[k] > x:
                s += p[k] * count[k]
        print(s)