# Write a function called "findAllSmall" that takes one list of integers and another integer as input, and returns an list of integers that contains all elements that are smaller than the input integer.

def findAllSmall(lst, num):
    result = []
    for ele in lst:
        if ele < num:
            result.append(ele)
    return result


print(findAllSmall([1, 2, 3], 10))
print(findAllSmall([1, 2, 3], 2))
print(findAllSmall([1, 3, 5, 4, 2], 4))
