"""
Find duplicate characters in a String and count the number of occurrences of the duplicate characters

"""

input_string = "abcdaddccwetiba"


def dup_chars(some_string):
    input_dict = {}
    dup_dict = {}
    input_list = list(some_string)
    print("input_list=", input_list)
    # create list from input strings
    for i in range(len(some_string)):
        input_dict[i] = some_string[i]
    print("input_dict=", input_dict)

    for i in range(len(input_list)):
        if input_list.count(input_list[i]) > 1:
            dup_dict[input_list[i]] = input_list.count(input_list[i])

    return dup_dict


def dup_value(some_string):
    input_list = list(some_string)
    print("input_list from dup_value=", input_list)
    input_dict = {}
    dup_dict = {}

    for index in range(len(input_list)):
        if input_list[index] in input_dict:
            input_dict[input_list[index]] += 1
        else:
            input_dict[input_list[index]] = 1

    for key, value in input_dict.items():
        if input_dict[key] > 1:
            dup_dict[key] = input_dict[key]

    return dup_dict


if __name__ == "__main__":
    dup_dict_main = dup_value(input_string)

    print("List of duplicates:", dup_dict_main)

    output_dup = {}
    output_dup = dup_chars(input_string)
    print("\nNumber of occurrences of duplicate characters\n:", output_dup)


