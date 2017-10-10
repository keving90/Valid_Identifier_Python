#/usr/bin/env python

"""is_valid_identifier.py (Kevin Geiszler) Determines if an indentifier is valid or not."""

import keyword

def IsValidIdentifier(string):
    """Determines if an indentifier is valid or not."""
    counter = 0
    if string in keyword.kwlist:
        feedback = (False, "Invalid: can't use a keyword as your identifier!")
        return feedback
    if not (string[0].isalpha() or string[0] == "_"):
        feedback = (False, "Invalid: first character must be alphabetic or underscore!")
        return feedback
    for letter in string[1:]:
        counter += 1
        if not (letter.isalnum() or letter == "_"):
            screen_out = "Invalid: character '%s' at index %d!" % (letter, counter)
            feedback = (False, screen_out)
            return feedback
    return (True, "Valid!")

if __name__ == '__main__':
    DATA = ('x', '_x', '2x', 'x,y', 'yield', 'is_this_good')
    for test in DATA:
        print test, "->", IsValidIdentifier(test)[1]

"""
$ hw07_1.py
x -> Valid!
_x -> Valid!
2x -> Invalid: first character must be alphabetic or underscore!
x,y -> Invalid: character ',' at index 1!
yield -> Invalid: can't use a keyword as your identifier!
is_this_good -> Valid!
$ """
