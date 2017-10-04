# find second largest number in array
array_input = [2, 3, 5, 7, 1, 0, 20, 15, 7]


def second_max(array):
    max1 = 1
    max2 = 0
    for each in array:
        if (each > max2) and (each <= max1):
            max2 = each
        if (each > max1) and (each >= max2):
            max2 = max1
            max1 = each
    return max2


if __name__ == "__main__":
    print("second max number = %s" % (second_max(array_input)))