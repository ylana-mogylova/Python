"""
Given a string S consisting of N characters. All characters are either open or close parentheses.
Check if the string is properly nested.
"""


def if_nested_string(parentheses_string):
    parentheses_dict = {}

    for i in range(len(parentheses_string)):
        if parentheses_string[i] in parentheses_dict:
            parentheses_dict[parentheses_string[i]] += 1
        else:
            parentheses_dict[parentheses_string[i]] = 1

    if len(parentheses_dict) < 2:
        return False
    elif parentheses_dict['('] == parentheses_dict[')']:
        return True
    else:
        return False


def nested_string(parentheses_string):
    open_parentheses = 0
    closed_parentheses = 0
    for i in range(len(parentheses_string)):
        if parentheses_string[i] == "(":
            open_parentheses += 1
        else:
            closed_parentheses += 1

    if open_parentheses == closed_parentheses:
        return True
    else:
        return False


if __name__ == "__main__":
    input_string_test = ["((()()(())()()))", "()", "))", "((", "((()))", "(())()"]
    for each in input_string_test:
        if if_nested_string(each):
            print("The string %s is properly nested" % each)
        else:
            print("The string %s is not properly nested" % each)
    print("---------------------------")
    for each in input_string_test:
        if nested_string(each):
            print("The string %s is properly nested" % each)
        else:
            print("The string %s is not properly nested" % each)