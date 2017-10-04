# the largest sum of consecutive integers in an array

input_array = [2, 3, 55, 1, 0, 10, 3, 2, 5, 27]


def largest_sum_consec_int(array):
    largest_sum = 0
    index = 0

    while index + 1 <= len(array) - 1:
        if array[index] + array[index + 1] > largest_sum:
            largest_sum = array[index] + array[index + 1]
        index+= 1
    return largest_sum


if __name__ == "__main__":
    print("largest sum of consecutive integers =", largest_sum_consec_int(input_array))