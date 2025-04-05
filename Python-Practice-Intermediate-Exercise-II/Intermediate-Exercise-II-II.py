# Write a function called "intersection" that takes 2 lists, and returns an list of elements that are in the intersection of 2 list.
# intersection 交集

def findintersection(lst1, lst2):
    return list(set(lst1).intersection(set(lst2)))


print(findintersection([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]))


def findintersection2(lst1, lst2):
    result = []

    for element1 in lst1:
        for element2 in lst2:
            if element1 == element2:
                result.append(element1)  # 或用 element2 都可以

    return result


print(findintersection2([1, 3, 4, 6, 10], [5, 11, 4, 3, 100, 144, 0]))
