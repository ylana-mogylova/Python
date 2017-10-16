"""
Given an array , find the element (say X) that has all the elements less that it to its left side and all the elements greater to it on its right side.
The left and right elements of X need not be in sorted form.
"""


def smaller_greater(matrix, number):
    left_matrix = []
    right_matrix = []

    for i in range(len(matrix)):
        if matrix[i] < number:
            left_matrix.append(matrix[i])
        elif matrix[i] > number:
            right_matrix.append(matrix[i])

    return left_matrix, right_matrix

if __name__ == "__main__":
    input_array = [7, 8, 1, 0, 5, 10, 15, 3, 6]
    x_element = 5
    smaller_elements, greater_elements = smaller_greater(input_array, x_element)
    print("Elements %s less than number %s" % (smaller_elements, x_element))
    print("Elements %s greater than number %s" % (greater_elements, x_element))