# Write a function called "stars" which prints out layers of stars in the following pattern:

def stars(n):
    stage_n = 1  # 計算目前的階段，也可以不用打印出來
    for i in range(1, n + 1):
        print('*' * i)
        stage_n += 1  # 因為 for 迴圈會自動加1，所以這行可以省略


stars(1)
stars(4)
