from random import random

# create list of 20 random floats between 0 and 1
values = [random() for i in range(20)]
# generate random threshold value x
x_threshold = random()

# sort list in ascending order
values.sort()

# Find where value is >= x
matching_indices = [i for i, val in enumerate(values) if val >= x_threshold]

print(f"Sorted List: {values}")
print(f"Value of x: {x_threshold}")

if matching_indices:
    print(f"First matching index: {matching_indices[0]}")
else:
    print("No matching index found.")