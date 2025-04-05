# Write a function that check if a list contains a subsequence of 007
# subsquence = 007 是指在這個 list 中藏著 007 但不用是連續的，只是順序一定要正確

def spyGame(lst):
    string = "007"
    pointer_for_lst = 0
    pointer_for_string = 0

    while pointer_for_lst < len(lst):
        # 假設對比相同，string 的 pointer 往後移動一位
        if lst[pointer_for_lst] == int(string[pointer_for_string]):
            pointer_for_string += 1
            # 偵測完成
            if pointer_for_string == len(string):
                return True

        pointer_for_lst += 1

    return False


print(spyGame([1, 2, 4, 0, 3, 0, 7]))
print(spyGame([1, 2, 5, 0, 3, 1, 7]))
print(spyGame([1, 2, 4, 0, 3, 0, 7, 0]))
