# Write a function called "findSmallerTotal" that takes one list of integers and one integer as input, and returns the sum of all elements in the list that are smaller than the input integer.

def findSmallerTotal(lst, num):
    total = 0
    for ele in lst:
        if ele < num:
            total += ele
    return total


print(findSmallerTotal([1, 2, 3], 3))
print(findSmallerTotal([1, 2, 3], 1))
print(findSmallerTotal([3, 2, 5, 8, 7], 999))
print(findSmallerTotal([3, 2, 5, 8, 7], 0))
