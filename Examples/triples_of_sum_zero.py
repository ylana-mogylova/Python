"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all triplets in the array which gives the sum of zero.
"""

matrix1 = [9, 8, -8, -1, 7, 6, 5, -13, 3, 7, -10, 8, 3, 70]
matrix2 = [-3, 3, 0, -1, -2, 2]


def sum_triplet_zero(array):
    output_array = []
    # create a dictionary from array
    dict_array = {}

    # for each in array:
    #     dict_array[array.index(each)] = each
    # print("dict_array=", dict_array)
    first_index = 0
    count = 0
    while first_index <= len(array) - 3:
        second_index = first_index + 1
        while second_index <= len(array) - 2:
            third_index = second_index + 1
            while third_index <= len(array) - 1:
                if array[first_index] + array[second_index] + array[third_index] == 0:
                    output_array.append((array[first_index], array[second_index], array[third_index]))
                count += 1
                third_index += 1

            second_index += 1
        first_index += 1
    return count, output_array


def sum_triplet_zero_sorted(array):
    array = sorted(array)
    result = 0

    for i in range(len(array) - 2):
        k = len(array) - 1
        for j in range(i + 1, len(array) - 1):
            while k >= 0 and array[i] + array[j] + array[k] == 0:
                k -= 1
            result += max(k, j) - j

    return result


def sum_triplet_zero_dic(array):
    output_array = []
    # create a dictionary from array
    dict_array = {}

    for next_index, each in enumerate(array):
        dict_array[next_index] = each

    first_index = 0
    count = 0

    for first_index in range(len(array)-1):
        for second_index in range(first_index + 1, len(array)):
            count += 1
            if 0 - (array[first_index] + array[second_index]) in dict_array.values():
                if {array[first_index], array[second_index], 0 - (array[first_index] + array[second_index])} not in output_array:

                    output_array.append(
                        {array[first_index], array[second_index], 0 - (array[first_index] + array[second_index])})

    return count, output_array

if __name__ == "__main__":
    print("Input array=", matrix1)
    main_count, triplet_array = sum_triplet_zero(matrix1)
    print("Triplets in the array which gives the sum of zero %s: \n number of iterations = %s" % (
        triplet_array, main_count))

    main_count, triplet_array = sum_triplet_zero_dic(matrix1)
    print("Triplets in the array which gives the sum of zero %s: \n number of iterations = %s" % (
        triplet_array, main_count))

