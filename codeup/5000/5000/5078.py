n = []
for i in range(3) :
    n.append(int(input()))
if n[0] == n[1] == n[2] == 60 :
    print("Equilateral")
elif n[0] + n[1] + n[2] != 180 :
    print("Error")
elif n[0] + n[1] + n[2] == 180 and n[0] == n[1] or n[1] == n[2] or n[2] == n[0] :
    print("Isosceles")
elif n[0] + n[1] + n[2] == 180 and n[0] != n[1] or n[1] != n[2] or n[2] != n[0] :
    print("Scalene")
elif n[0] + n[1] + n[2] != 180 :
    print("Error")