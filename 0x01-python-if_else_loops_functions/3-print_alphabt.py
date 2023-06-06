#!/usr/bin/python3
for asciiAlpha in range(97, 123):
    if asciiAlpha != 101 and asciiAlpha != 113:
        print("{:c}".format(asciiAlpha), end="")
