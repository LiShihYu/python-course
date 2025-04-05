# Write a function called "printMany" that prints out integers 1, 2, 3, ..., 100.

def printMany():
    for i in range(1, 101):
        print(i)
        i += 1  # 這行其實可以省略，因為 for 迴圈會自動加 1


printMany()  # 如果打成 print(printMany()) 再輸出結果會多出一個 None，因此要改成 printMany() 就好
