# Write a function called "palindrome" that checks if the input string is a palindrome. (Search on google if you don't know what a palindrome is.)
# palindrome 迴文：正著讀與倒著讀都是一樣的

# 適用於教學用途或固定比對string的情況下
import math


def palindrome(string):

    # for loop
    # math.floor() 取整數
    for i in range(0, math.floor(len(string) / 2)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True


print(palindrome("bearaeb"))
print(palindrome("Whatever revetahW"))
print(palindrome("Aloha, how are you today?"))

# lefr += 1  right -= 1
# stop while loop when left is bigger than right
# 適用於效能導向、資料量大、記憶體有限的情況下


def palindrome2(string):

    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


# 適用於程式競賽、寫簡潔小工具的情況下
def palindrome3(string):
    if string == string[::-1]:
        return True
    return False
