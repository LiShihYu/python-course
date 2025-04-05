# Write a function called "inversePyramid" that draws pyramid upside down.

def inversePyramid(num):
    space = 0
    star = 2 * num - 1

    for i in range(num):
        print(space * ' ' + star * '*')
        star -= 2
        space += 1


# 不建議這樣做，因為這樣會改變原本的 pyramid 函數的功能
def inversePyramid2(m):
    result = []

    def pyramid(num):
        space = num - 1
        star = 1

        for i in range(num):
            result.append(space * ' ' + star * '*')
            star += 2
            space -= 1

    pyramid(m)
    result.reverse()

    # 將反轉後的金字塔一行一行 print 出來
    for line in result:
        print(line)


inversePyramid2(4)
