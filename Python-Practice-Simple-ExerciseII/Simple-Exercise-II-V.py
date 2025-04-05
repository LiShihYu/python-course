# Write a function called "swap" that takes a string as input, and returns a new string with lowercase changed to uppercase, uppercase changed to lowercase.

def swap(str):
    result = ""
    for ele in str:
        if ele.isupper():
            result += ele.lower()
        elif ele.islower():
            result += ele.upper()
        else:
            # 針對不是英文字母的字元，就直接原封不動的加到結果裡面
            result += ele

    print(result)
    return result


swap("Aloha")
swap("Love you.")
