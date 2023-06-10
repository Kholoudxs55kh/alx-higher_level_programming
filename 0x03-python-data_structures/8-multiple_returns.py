#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        _tuple = (len(sentence), sentence[0])
    else:
        _tuple = (0, None)
    return _tuple
