# Write a function called "stars2" which prints out layers of stars in the following pattern:

def stars2(n):
    for i in range(1, n + 1):
        print('*' * i)
    for i in range(n - 1, 0, -1):
        print('*' * i)


stars2(1)
stars2(2)
stars2(3)
stars2(4)
