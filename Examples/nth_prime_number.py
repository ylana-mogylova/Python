"""
Write a function that returns the nth prime number in a series of natural numbers.
"""

natural_array = range(1, 100)
nth_number = 11


def nth_prime_number(input_array, prime_index):
    counter = 0

    for each in input_array:
        flag = False

        for number in range(each - 1):
            if number > 1:
                if each % number == 0:
                    flag = True
                    break
        if not flag and each > 1:
            counter += 1
        if counter == prime_index:
            return each


if __name__ == "__main__":
    i = nth_prime_number(natural_array, nth_number)
    print("%s prime number of array %s is %s" % (nth_number, natural_array, i))
