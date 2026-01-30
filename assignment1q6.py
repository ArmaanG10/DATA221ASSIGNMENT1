def distribution_analysis(numbers_list):

    total_count = len(numbers_list)
    # get unique values and sort them to ensure the dictionary is sorted by key
    unique_sorted_keys = sorted(list(set(numbers_list)))

    distribution_dict = {}

    for key in unique_sorted_keys:
        # Count how many numbers in the original list are less than or equal to the key
        count_le = sum(1 for x in numbers_list if x <= key)
        # calculate percentage
        percentage = (count_le / total_count) * 100
        distribution_dict[key] = percentage

    return distribution_dict


# example input
input_numbers = [3, 1, 2, 3, 4, 2]
print(distribution_analysis(input_numbers))