# Write a function called "position" that returns a tuple of the first uppercase letter and its index location. If not found, returns -1.

def position(string):

    # enumerate()：遍歷可迭代的 object，並同時獲取索引和對應的值
    for num, s in enumerate(string):
        # 也可以寫成 if s.isupper()，但這樣會比較慢，因為 isupper() 會檢查每個字母是否是大寫字母
        if s == s.upper():
            return (s, num)
    return -1


print(position("abcd"))
print(position("ABcd"))
print(position("abCD"))
