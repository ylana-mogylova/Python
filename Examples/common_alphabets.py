"""
You are given 2 strings: string, strong. Find the common alphabets in two strings and print it.
i/p: string , strong
o/p: strng
"""


def common_alphabets(s1, s2):
    common_letters = ""

    if len(s1) <= len(s2):
        for char in s1:
            if char in s2:
                common_letters += char
    else:
        for char in s2:
            if char in s1:
                common_letters += char

    return common_letters


if __name__ == "__main__":

    input_strings = [("string", "strong"), ("abc", "abcsewe"), ("abcdefgh", "cfgw")]
    for each_pair in input_strings:
        print("Common alphabets in two strings %s and %s is %s" % (
        each_pair[0], each_pair[1], common_alphabets(each_pair[0], each_pair[1])))
