a = input()
if a[-1] == "2" and a != "12" :
    print(a + "nd")
elif a[-1] == "1" and a != "11" :
    print(a + "st")
elif a[-1] == "3" and a != "13" :
    print(a + "rd")
else :
    print(a + "th")