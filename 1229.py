a,b = map(float,input().split())
if a >= 160 :
	a = (a - 100) * 0.9
elif a >= 150 :
	a = (a - 150) / 2 + 50
else :
	a -= 100
r = (b - a) * 100 / a
if r > 20 :
	print("비만")
elif r > 10 :
	print("과체중")
else :
	print("정상")