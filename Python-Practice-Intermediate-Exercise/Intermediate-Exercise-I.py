# Write a function called "mySort" that takes an list of integers as input, and returns the sorted version of the input list. You are not allowed to use the built-in sorted() function.

def findMin(lst):
    if not lst:
        return "undefined"

    result = lst[0]

    for ele in lst:
        if ele < result:
            result = ele

    return result


def mySort(myList):

    result_list = []

    while len(myList) > 0:
        # 利用 findMin() function 找出最小值
        min_value = findMin(myList)
        # 加入到 result_list 中
        result_list.append(min_value)\
            # 再從 myList 中移除最小值
        myList.remove(min_value)

    print(result_list)
    return result_list


mySort([17, 0, -3, 2, 1, 0.5])


# 如果直接利用 插入排序 (Insertion Sort) 會更快一點
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    print(arr)
    return arr


insertion_sort([17, 0, -3, 2, 1, 0.5])
