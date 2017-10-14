
input_string = "abcdaddccwetiba"
desired_keys = []

input_dict = {}
dup_dict = {}
# create dictionary from input string
for i in range(len(input_string)):
    input_dict[i] = input_string[i]
print("input_dict=", input_dict)

d = {}
for k, v in input_dict.items():
    d.setdefault(k,set())
    d[k].add(v)
print("d=", d)

