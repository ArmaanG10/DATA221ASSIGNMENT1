def create_string_info_dict(string_list):
    result_dict = {}
    for s in string_list:
        # calculate length of string
        length_of_string = len(s)
        # check if length is even/odd
        parity_type = "even" if length_of_string % 2 == 0 else "odd"

        result_dict[s] = {"length": length_of_string, "parity": parity_type}

    return result_dict


# test data
words = ["data", "science"]
output = create_string_info_dict(words)

print("{")
for key, value in output.items():
    print(f'  "{key}": {value},')
print("}")