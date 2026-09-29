k =  {
    "1" : 400,
    "2" : 340,
    "3" : 170,
    "4" : 100,
    "5" : 70,
}

a,b = map(str, input().split())
if k[a] + k[b] > 500 :
    print("angry")
else :
    print("no angry")