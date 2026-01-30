# the limit we don't want the product to exceed
threshold = 100
# starting point for multiplication
product = 1
# the integer we go up by each step
current_number = 1

# Continue multiplying as long as the product is below or equal to the threshold
while product <= threshold:
    current_number += 1
    product *= current_number

# final output
print(f"Final Product: {product}")
print(f"Integer that caused the product to exceed the threshold: {current_number}")