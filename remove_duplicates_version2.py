def remove_duplicates(array):
    duplicates = []
    array_without_duplicates = []
    copylist = []

    for item in array:
        if item in copylist:
            if item not in duplicates:
                duplicates.append(item)

        copylist.append(item)

    for item in array:
        if item not in duplicates:
            array_without_duplicates.append(item)

    return duplicates, array_without_duplicates


if __name__ == "__main__":
    str_array_input = input('Enter your array:')
    input_str_list = str.split(str_array_input, ",")
    input_list = []
    list_duplicates = []
    no_duplicates = []
    for each in input_str_list:
        input_list.append(int(each.replace(" ", "")))

    print("input array=", input_list)

    list_duplicates, no_duplicates = remove_duplicates(input_list)

    print("list of duplicates = %s, list without duplicates = %s" % (list_duplicates, no_duplicates))
