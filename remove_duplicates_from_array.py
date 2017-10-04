# write a program to remove duplicates numbers from the list and display the duplicates plus display original
# array without duplicates


def remove_duplicates(array):
    duplicates = set()
    copylist = set()

    for item in array:
        if item in copylist:
            if item not in duplicates:
                duplicates.add(item)
        else:
            copylist.add(item)

    return duplicates, copylist


if __name__ == "__main__":
    str_array_input = input('Enter your array:')
    input_str_list = str.split(str_array_input, ",")
    input_list = []
    list_duplicates = set()
    no_duplicates = set()
    for each in input_str_list:
        input_list.append(int(each.replace(" ", "")))

    print("input array=", input_list)

    list_duplicates, no_duplicates = remove_duplicates(input_list)

    print("list of duplicates = %s, list without duplicates = %s" % (list_duplicates, no_duplicates))