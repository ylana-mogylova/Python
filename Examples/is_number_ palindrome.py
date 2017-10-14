
def digit_palidrome(input_number):
    n = input_number
    rev = 0
    while input_number > 0:
        dig = input_number % 10
        rev = rev * 10 + dig
        input_number = input_number // 10

    if n == rev:
        return True
    else:
        return False

if __name__ == "__main__":
    num = [2222, 2112, 33, 989, 1, 78346, 45879, 2121212]
    for each in num:
        if digit_palidrome(each):
            print("digit %s is a palidrome" % each)
        else:
            print("digit %s is not a palidrome" % each)