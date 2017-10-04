"""
Write code to remove duplicates from an unsorted linked list
"""

input_list = [1, 2, 1, 3, 2, 5, 5, 7]


def remove_duplicates_set(input_user_list):
    no_duplicates = set()
    for each in input_user_list:
        if each not in no_duplicates:
            no_duplicates.add(each)
    return no_duplicates


def remove_duplicates_list(input_user_list):
    no_duplicates = list()

    for index, each in enumerate(input_user_list):
        if each not in no_duplicates:
            no_duplicates.append(each)
    return no_duplicates


def remove_duplicates_one_line(input_user_list):
    return list(set(input_user_list))


if __name__ == "__main__":
    print("List without duplicates set:", remove_duplicates_set(input_list))
    print("List without duplicates list:", remove_duplicates_list(input_list))
    print("List without duplicates list one line:", remove_duplicates_one_line(input_list))
