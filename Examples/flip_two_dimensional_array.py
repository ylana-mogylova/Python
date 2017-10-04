"""
flip two dimensional array
[2, 3, 4, 2, 3, 5]
[3, 5, 6, 7, 8, 9]
[45, 64, 35, 67, 46, 53]
"""

initial_matrix = [[2, 3, 4, 2, 3, 5], [3, 5, 6, 7, 8, 9], [45, 64, 35, 67, 46, 53]]


def flip_array(matrix):
    index_row = 0

    flip_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    while index_row < len(matrix):
        index_col = 0
        while index_col < len(matrix[index_row]):
            flip_matrix[index_col][index_row]= matrix[index_row][index_col]
            index_col += 1

        index_row += 1
    return flip_matrix


def flip_array_for(matrix):
    flip_matrix = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for index_row in range(len(matrix)):
        for index_col in range(len(matrix[index_row])):
            flip_matrix[index_col][index_row]= matrix[index_row][index_col]
            index_col += 1
    return flip_matrix

if __name__ == "__main__":
    print("initial_array:")

    for i in range(len(initial_matrix)):
        print(initial_matrix[i])

    print("flipped array:")
    flipped_array = flip_array(initial_matrix)

    for i in range(len(flipped_array)):
        print(flipped_array[i])

    print("flipped array using for:")
    flipped_array_for = flip_array_for(initial_matrix)

    for i in range(len(flipped_array_for)):
        print(flipped_array_for[i])
