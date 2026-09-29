n = int(input())
r = n * 5000
if n >= 5 :
    r -= r * 0.1
    r = int(r)
print(f"딸기의 가격은 {r}원 입니다.")