import math


def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):

    # check if radii are positive integers
    if not (isinstance(radiusOfCircle1, int) and isinstance(radiusOfCircle2, int)):

        return "Error: Both radii must be integers."
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:

        return "Error: Both radii must be positive integers."

    # compute area of each circle using: A = pi * r^2
    area1 = math.pi * (radiusOfCircle1 ** 2)
    area2 = math.pi * (radiusOfCircle2 ** 2)

    # identify the smaller and larger areas
    smaller_area = min(area1, area2)
    larger_area = max(area1, area2)

    # return the percentage of the larger circle covered by the smaller one
    coverage_percentage = (smaller_area / larger_area) * 100
    return f"{coverage_percentage:.2f}%"

try:

    user_radius1 = int(input("Enter the radius for the first circle: "))
    user_radius2 = int(input("Enter the radius for the second circle: "))

    # call function using users inputs
    result = circleAreaCoverage(user_radius1, user_radius2)

    # display final result
    print(f"Coverage Result: {result}")

except ValueError:
    # This catches cases where the user types something that isn't a number
    print("Invalid input! Please enter whole numbers only.")