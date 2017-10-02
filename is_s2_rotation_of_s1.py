"""
Assume you have a method isSubstring which checks if one word is a isSubstring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only
one call to isSubstring(e.g., "waterbottle" is a rotation of "erbottlewat").
"""


def is_substring(s2, s1):
    if s2 in s1:
        return True
    else:
        return False


def is_rotation_substring(s1, s2):
    string_big = s1 + s1
    if is_substring(s2, string_big):
        return True
    else:
        return False


if __name__ == "__main__":
    list_of_inputs = [("waterbottle", "erbottlewat"), ("waterbottle", "aterbottlew"), ("waterbottle", "ewaterbottl"),\
                      ("waterbottle", "awterbottlew")]
    for each_tuple in list_of_inputs:
        s1 = each_tuple[0]
        s2 = each_tuple[1]
        if is_rotation_substring(s1, s2):
            print("Substring %s is a rotation of %s" % (s2, s1))
        else:
            print("Substring %s is not a rotation of %s" % (s2, s1))

