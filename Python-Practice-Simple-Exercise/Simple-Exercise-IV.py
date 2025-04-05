# Write a function called "findSmallCount" that takes one list of integers and one integer as input, and returns an integer indicating how many elements in the list is smaller than the input integer.

def findSmallCount(lst, num):
    count = 0
    for ele in lst:
        if ele < num:
            count += 1
    return count


print(findSmallCount([1, 2, 3], 2))
print(findSmallCount([1, 2, 3, 4, 5], 0))
