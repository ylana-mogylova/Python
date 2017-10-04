"""
write a program where a there are multiple users logging into the system or file
and I want to know the login Occurrences of the each user .
Note : The file is separated by the commas. ex: User1 , User2, user1 , user3.........
"""
# User1, User2, user1, user3, user1, user4, user5, User3, user2, user6, user6, user1

import easygui


def login_occurrence_dict(input_file):
    file_to_string = ""
    login_list = []
    occurrence_dict = {}
    # convert file to the list
    num_file_lines = sum(1 for line in input_file)
    input_file.seek(0)
    if num_file_lines == 1:
        file_to_string = input_file.readline()
        login_list = file_to_string.split(',')
    else:
        file_to_string = input_file.readlines()
        for index, each_line in enumerate(file_to_string):
            login_list = login_list + file_to_string[index].split(',')

    # create dict of login occurrences
    for i in login_list:
        if i.lower().strip() in occurrence_dict:
            occurrence_dict[i.lower().strip()] += 1
        else:
            occurrence_dict[i.lower().strip()] = 1
    return occurrence_dict

if __name__ == "__main__":
    path = easygui.fileopenbox()
    f = open(path, 'r')
    print("Occurences of login:\n", login_occurrence_dict(f))