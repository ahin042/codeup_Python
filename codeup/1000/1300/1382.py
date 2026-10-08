for i in range(1, 10):
    for j in range(2, 6):
        print(f"{j} x {i} = {j * i:2d}", end='')
        if j < 5:
            print('\t', end='')
    print()