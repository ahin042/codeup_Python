n = input()
lst = input()
m = {} ; c = 0 ; r = ""
for i in n :
    m[i] = c
    c += 1
for i in lst :
    if i == " " :
        r += " "
    else :
        r += str(m[i])
print(r)