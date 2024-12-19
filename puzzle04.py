def remove_vowels(input_str):
    vowels = "aeiouAEIOU"
    result = "".join(char for char in input_str if char not in vowels)
    return result

input_str = "hello world"
print(remove_vowels(input_str))