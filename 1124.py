n = input().strip()
p = n.split('H')
cs = p[0].replace('C', '')
c = int(cs) if cs != "" else 1
hs = p[1]
h = int(hs) if hs != "" else 1
r = (c * 12) + (h * 1)
print(r)