# Write a function called "flatten" that flattens an list.
# flatten 扁平化

result = []


def flatten(lst):
    for i in lst:
        # 檢查一個東西是不是 list
        if type(i) == type([]):
            flatten(i)
        else:
            result.append(i)

    return result


print(flatten([1, [[], 2, [0, [1]], [3]], [1, 3, [3], [4, [1]], [2]]]))
