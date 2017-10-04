"""
give a list of information for people (age, weight, height) sort by people height
"""

people_information = [(23, 60, 170), (30, 84, 180), (15, 70, 150)]


def sort_by_height(people_list):
    index_external_loop = 0
    while index_external_loop <= len(people_list) - 2:
        min_index = index_external_loop
        index_next = index_external_loop + 1
        while index_next <= len(people_list) - 1:
            if people_list[index_next][2] < people_list[min_index][2]:
                min_index = index_next
            index_next += 1

        temp = people_list[index_external_loop]
        people_list[index_external_loop] = people_list[min_index]
        people_list[min_index] = temp

        index_external_loop += 1

    return people_list


if __name__ == "__main__":
    print("Sorted by height list of people:\n", sort_by_height(people_information))
    people_information.sort(key=lambda tup: tup[2])
    print("Sorted by height list of people:\n", people_information)