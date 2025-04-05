# Given a list of ints, return True if the list contains a 3 next to a 3.

# for loop index == index + 1
def has_33(nums):
    result = False

    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            result = True
    return result


print(has_33([1, 5, 7, 3, 3]))
print(has_33([]))
print(has_33([4, 3, 2, 1, 0]))


def has2_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


print(has2_33([1, 5, 7, 3, 3]))
print(has2_33([]))
print(has2_33([4, 3, 2, 1, 0]))
