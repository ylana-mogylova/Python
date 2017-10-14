"""
Given two sorted arrays A and B that may have repeated elements. Form a new sorted array C that contains the elements of A and B
[Condition : You are not allowed to merge the two arrays and then sort. ]
"""


def merge_sorted_arrays(array1, array2):
    merge_array = []
    i = 0
    j = 0

    while i < len(array1):
        while j < len(array2):
            if array1[i] < array2[j]:
                merge_array.append(array1[i])
                i += 1
                break
            elif array1[i] == array2[j]:
                merge_array.append(array1[i])
                i += 1
                merge_array.append(array2[j])
                j += 1
                break
            else:
                merge_array.append(array2[j])
                j += 1
        if j == len(array2):
            break

    if i < len(array1):
        while i < len(array1):
            merge_array.append(array1[i])
            i += 1
    if j < len(array2):
        while j < len(array2):
            merge_array.append(array2[j])
            j += 1

    return merge_array


if __name__ == "__main__":
    first_array = [0, 2, 3, 5, 6, 7, 8, 87]
    second_array = [0, 2, 7, 8, 10, 23, 100, 123]
    print("Merged array=", merge_sorted_arrays(first_array, second_array))