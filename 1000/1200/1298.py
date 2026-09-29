import math

a,b,c = map(int, input().split())
if a < 0:
    a, b, c = -a, -b, -c
if a == 0 and b == 0:
    print("0 0" if c == 0 else "Not Exist")
elif a == 0:
    print(f"0 {c // b}" if c % b == 0 else "Not Exist")
elif b == 0:
    print(f"{c // a} 0" if c % a == 0 else "Not Exist")
else:
    d = math.gcd(a, b) # 최대공약수
    if c % d == 0:
        a //= d
        b //= d
        c //= d
        try:
            r = abs(b) # 절댓값
            x = (c * pow(a, -1, r)) % r # 거듭제곱
            if x <= 0:
                x += r
            y = (c - a * x) // b
            print(f"{x} {y}")
        except ValueError:
            print("Not Exist")
    else:
        print("Not Exist")