a = int(input())
aa = list(map(int, input().split()))
r1 = False ; r2 = False
for i in range(len(aa) - 1) :
    if aa[i] < aa[i+1]:
        r1 = True
    if aa[i] > aa[i+1] :
        r2 = True
if r1 and not r2 :
    print("오름차순")
elif r2 and not r1:
    print("내림차순")
else:
    print("섞임")