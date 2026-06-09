def prime(n):
    if n <= 1:
        return "composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "composite"
    return "prime"
n = int(input())
print(prime(n))