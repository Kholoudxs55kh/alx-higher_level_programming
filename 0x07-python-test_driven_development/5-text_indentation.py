#!/usr/bin/python3
""" 5th Task """


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text is "\n":
        print()
    """
    for char in text:
        print(char, end="")
        if char in ('.', '?', ':'):
            print("\n\n", end="")
    """

    new_str = ""
    for char in text:
        new_str += char

        if char in ('.', '?', ':'):
            print(new_str.strip())
            print()
            new_str = ""
    print(new_str.strip(), end='')
