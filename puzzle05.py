def get_longest_str(input_str):
    if not input_str:
        return ""
    
    longest_str = max(input_str,key=len)
    return longest_str

input_str = ["cat","orange","blue","potato"]
print(get_longest_str(input_str))
