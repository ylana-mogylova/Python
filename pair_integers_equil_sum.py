# print out pair of integers sum of which equal to key sum
array = list(range(1, 11))
pairs = []
key_sum = 7

for number in array:

    number_index = array.index(number)

    for next_number in array[number_index+1:]:

        if number + next_number == key_sum:
            pairs.append((number, next_number))

print("pairs: %s" % pairs)