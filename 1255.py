a, b = map(float, input().split())
while a <= b + 1e-9:  # 부동소수점 오차 보정
    print(f"{a:.2f}", end=" ")
    a += 0.01