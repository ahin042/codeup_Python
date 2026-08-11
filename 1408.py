a = input()
for i in a :
    print(chr(ord(i) + 2), end="")
print()
for i in a :
    print(chr((ord(i) *7) % 80 + 48), end="")