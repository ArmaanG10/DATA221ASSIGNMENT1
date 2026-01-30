def convert_seconds_to_time(total_seconds):

    # check if seconds are in 24 hour range (0 to 86399)
    if not isinstance(total_seconds, int) or total_seconds < 0 or total_seconds >= 86400:
        return "Invalid input. Please provide seconds between 0 and 86399."

    # calculate hours, minutes, and seconds

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    # check for AM or PM
    period = "AM" if hours < 12 else "PM"

    # Convert 24 hour time to 12 hour format
    display_hours = hours % 12
    if display_hours == 0:
        display_hours = 12

    # format
    return f"{display_hours} {minutes} {seconds} {period}"

try:

    user_input = input("Enter the number of seconds since midnight: ")

    total_seconds_input = int(user_input)

    formatted_time = convert_seconds_to_time(total_seconds_input)

    print(f"Converted Time: {formatted_time}")

except ValueError:
    # if the user enters text or a decimal instead of an integer
    print("Error: Please enter a valid whole number for seconds.")