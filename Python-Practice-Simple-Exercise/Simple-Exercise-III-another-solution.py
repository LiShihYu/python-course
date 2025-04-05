# 原本題目要求是「第一個大寫字母與其索引位置」，但如果我們希望找到「最後一個大寫字母與其索引位置」，要怎麼做?

def position(string):
    # 由於 enumerate 不能直接反向迭代，因此我們利用 range 來遍歷字串的索引
    for index in range(len(string) - 1, -1, -1):
        if string[index].isupper():
            return string[index], index
    return -1


print(position("abcd"))
print(position("ABcd"))
print(position("abCD"))
