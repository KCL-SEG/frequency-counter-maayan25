"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        key = str(item)
        if key in frequencies.keys():
            val = frequencies[key] + 1
            frequencies[key] = val
        else:
            frequencies[key] = 1
    return frequencies
