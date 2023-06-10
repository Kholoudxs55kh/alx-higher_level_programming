#!/usr/bin/python3
def multiple_returns(sentence):
    _tuple = (len(sentence), sentence[0] if sentence is not None else None)
    return _tuple
