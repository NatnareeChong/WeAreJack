#! /usr/bin/env python3
"""Simple test of colors."""

from termcolor import colored

text = colored('Hi this is green', 'green') + ". This is normal. " + colored(
                "This is red", 'red')
print(text)
