# input_string = aabbbccccaaa, maintain the insertion order and output should be a2b3c4a3
input_string = "aabbbccccaaa"


def insertion_number(s):
    output_string = ""

    index = 0
    flag = False
    char_number = 0
    while index < len(s):

        if not flag:
            char_number = 1
        if index < len(s)-1:
            if s[index] == s[index + 1]:
                char_number += 1

                flag = True
            else:
                flag = False

                output_string = output_string + s[index] + str(char_number)
        else:
            output_string = output_string + s[index] + str(char_number)

        index += 1

    return output_string


if __name__ == "__main__":
    print("output_string=", insertion_number(input_string))