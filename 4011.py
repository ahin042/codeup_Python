a,b = map(str, input().split("-"))
if b[0] == "1" :
    print(f"19{a[:2]}/{a[2:4]}/{a[4:]} M")
elif b[0] == "2" :
    print(f"19{a[:2]}/{a[2:4]}/{a[4:]} F")
elif b[0] == "3" :
    print(f"20{a[:2]}/{a[2:4]}/{a[4:]} M")
else :
    print(f"20{a[:2]}/{a[2:4]}/{a[4:]} F")