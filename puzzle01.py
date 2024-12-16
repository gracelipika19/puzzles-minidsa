def filter_strings_containing_a(input_strs):
    return [s for s in input_strs if 'a' in s]

input_list = ["apple","banana","cherry","date"]
result = filter_strings_containing_a(input_list)
print(result)