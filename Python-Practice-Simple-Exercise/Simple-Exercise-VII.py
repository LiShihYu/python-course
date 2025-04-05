# Write a function called "summ" that takes one list of numbers, and return the sum of all elements in the input list.

def summ(lst):
    total = 0
    for ele in lst:
        total += ele
    return total


print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(summ([]))
print(summ([-10, -20, -30]))
