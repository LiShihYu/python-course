# Write a function called "table" which takes an input n, and prints out n x 1 to n x 9

def table(n):
    for i in range(1, 10):
        n * i
        print(f"{n} * {i} = {n * i}")


table(3)
