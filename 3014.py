def solve(sum):
    if len(sum) <= 1:
        return sum
    m = len(sum) // 2
    ll = solve(sum[:m])
    rr = solve(sum[m:])
    r = []
    i = j = 0
    while i < len(ll) and j < len(rr):
        if ll[i] <= rr[j]:
            r.append(ll[i])
            i += 1
        else:
            r.append(rr[j])
            j += 1
    r.extend(ll[i:])
    r.extend(rr[j:])
    return r

a = int(input())
n = list(map(int, input().split()))
c = solve(n)
print(*c)