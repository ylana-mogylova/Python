"""
how to fetch telephone number and evmail address and copy it in another file
name: uliana; last_name: mogylova; email: ylana@gmail.com; phone number: 403-478-9747
name: steven; last_name: elliott; email: steven@gmail.com; phone number: 403-901-9747
name: brady; last_name: elliott; email: brady@gmail.com; phone number: 604-478-9747
"""

import easygui
import os


def fetch_email_phone(file_path, people_file):

    email_phone_file = open(os.path.join(file_path, 'email_phone.txt'), 'w')

    for each_line in people_file:
        new_file_string = ''
        each_line_list = each_line.split(';')
        for each_data_pair in each_line_list:
            if 'email' in each_data_pair:
                new_file_string = new_file_string + each_data_pair
            if 'phone number' in each_data_pair:
                new_file_string = new_file_string + ';' + each_data_pair

        email_phone_file.write(new_file_string)
    email_phone_file.close()


def fetch_email_phone_dict(file_path, people_file):

    email_phone_file = open(os.path.join(file_path, 'email_phone_dict.txt'), 'w')
    dict_of_one_file_line = {}
    for each_line in people_file:
        dict_of_one_file_line.clear()
        new_file_string = ''
        each_line_list = each_line.split(';')

        for each in each_line_list:
            dict_key, dict_value = each.split(":")
            dict_of_one_file_line[dict_key.strip()] = dict_value.strip()

        new_file_string = new_file_string + 'email: ' + dict_of_one_file_line['email']
        new_file_string = new_file_string + '; phone number: ' + dict_of_one_file_line['phone number'] + '\n'

        email_phone_file.write(new_file_string)
    email_phone_file.close()

if __name__ == "__main__":

    file_path_input = easygui.fileopenbox()
    input_file = open(file_path_input, 'r')
    file_path, file_name = os.path.split(file_path_input)
    fetch_email_phone(file_path, input_file)
    f = open(os.path.join(file_path, 'email_phone.txt'), 'r')

    for line in f:
        print(line)

    input_file = open(file_path_input, 'r')
    file_path, file_name = os.path.split(file_path_input)
    fetch_email_phone_dict(file_path, input_file)
    f_dict = open(os.path.join(file_path, 'email_phone_dict.txt'), 'r')
    for line in f_dict:
        print(line)