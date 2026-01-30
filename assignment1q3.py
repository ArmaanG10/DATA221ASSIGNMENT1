def compute_power(base_x, exponent_y):

    return base_x ** exponent_y

# list of pairs [x, y]
pairs = [[5, 2], [3, 1], [4, 3], [2, 0], [10, -2]]
valid_results = []

for x, y in pairs:
    # check if exponent is negative
    if y < 0:
        continue
    # store the result if pair is valid
    result = compute_power(x, y)
    valid_results.append(result)

print(f"Valid results: {valid_results}")