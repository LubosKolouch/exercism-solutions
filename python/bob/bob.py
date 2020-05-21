""" excercism.io Python track, task Bob"""
import re


def response(hey_bob):
    """ Craft the response """
    if re.search(r'^\n*\r*\s*$', hey_bob):
        return 'Fine. Be that way!'

    if re.search(r'[a-z]', hey_bob.lower()) and hey_bob == hey_bob.upper():
        if re.search(r'\?$', hey_bob):
            return 'Calm down, I know what I\'m doing!'
        return 'Whoa, chill out!'

    if re.search(r'\?\s*$', hey_bob):
        return 'Sure.'

    return 'Whatever.'
