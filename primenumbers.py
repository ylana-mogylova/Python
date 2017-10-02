# find all prime numbers from 1 to 100
array = range(1, 100)
prime_numbers = []

for each in array:
    flag = False
    for number in range(each - 1):
        if number > 1:
            if each % number == 0:
                flag = True
                continue

    if not flag:
        prime_numbers.append(each)

print("prime numbers from (1, 100): %s" % prime_numbers)