a = int(input())
n = list(map(int, input().split()))
if n == sorted(n):
    print("오름차순")
elif n == sorted(n, reverse=True) :
    print("내림차순")
else :
    print("섞임")