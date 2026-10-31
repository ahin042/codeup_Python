n = int(input())
def fun(k):
    if k > 1:
        fun(k // 2)
    print(k % 2, end='')
fun(n)