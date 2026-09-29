def p(x):
    for i in range(2, x):
        if x % i == 0:
            return "이벤트 실패"
    return "이벤트 성공"
print(p(int(input())))