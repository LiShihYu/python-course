# Write a function called "findMin" which takes an list as input, and returns the minimum element in the input list.

def findMin(lst):
    # 先檢查 function 是否為 empty list
    if not lst:
        print("undefined")
        return "undefined"

    min_value = lst[0]

    for num in lst:
        if num < min_value:
            min_value = num

    print(min_value)
    return min_value


findMin([1, 2, 5, 6, 99, 4, 5])
findMin([])
findMin([1, 6, 0, 33, 44, 88, -10])
