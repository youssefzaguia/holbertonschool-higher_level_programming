#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        first_char = None
    else:
        first_char = sentence[0]
    sentence_length = len(sentence)
    return (first_char, sentence_length)
