# Write a function called "pyramid" that takes an integer as input, and prints a pyramid in the following pattern:
# pyramid 金字塔

def pyramid(num):
    # 計算空格數量
    space = num - 1
    star = 1

    for i in range(num):
        print(space * ' ' + star * '*')
        star += 2
        space -= 1


pyramid(20)
