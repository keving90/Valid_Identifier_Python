#/usr/bin/env python

"""get_validity.py (Kevin Geiszler) Interactive identifier validater. Enter a blank line to quit. """

import is_valid_identifier as ivi

help(ivi)

def main():
    while True:
        response = raw_input("Enter the name of an identifier to have it validated: ")
        if not response:
            break
        print response, "->", ivi.IsValidIdentifier(response)[1]

if __name__ == '__main__':
    main()

"""
Help on module hw07_1:

NAME
    hw07_1 - hw07_1.py by Kevin Geiszler -- Determines if an indentifier is valid or not

FILE
    /Users/Kevin/Desktop/hw07_1/hw07_1.py

FUNCTIONS
    IsValidIdentifier(string)
        Determines if an indentifier is valid or not

Enter the name of an identifier to have it validated: hello
hello -> Valid!
Enter the name of an identifier to have it validated: 1type
1type -> Invalid: first character must be alphabetic or underscore!
Enter the name of an identifier to have it validated: _number
_number -> Valid!
Enter the name of an identifier to have it validated: steve!
steve! -> Invalid: character '!' at index 5!
Enter the name of an identifier to have it validated: fish5
fish5 -> Valid!
Enter the name of an identifier to have it validated: hello world
hello world -> Invalid: character ' ' at index 5!
Enter the name of an identifier to have it validated: hello_world
hello_world -> Valid!
Enter the name of an identifier to have it validated: Christmas
Christmas -> Valid!
Enter the name of an identifier to have it validated: 
$ """
