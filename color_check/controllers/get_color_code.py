# This file should contain a function called get_color_code().
# This function should take one argument, a color name,
# and it should return one argument, the hex code of the color,
# if that color exists in our data. If it does not exist, you should
# raise and handle an error that helps both you as a developer,
# for example by logging the request and error, and the user,
# letting them know that their color doesn't exist.
import json


with open('color_check/data/css-color-names.json') as f:
    color_code = json.load(f)

print(color_code)


def get_color_code(user_submitted_string):
    # this is where you should add your logic to check the color.
    # Open the file at data/css-color-names.json, and return the hex code
    # The file can be considered as JSON format, or as a Python dictionary.
    for key in color_code:
        if key == user_submitted_string:
            print(color_code[user_submitted_string])

    hex_code = color_code[user_submitted_string]

    return hex_code
