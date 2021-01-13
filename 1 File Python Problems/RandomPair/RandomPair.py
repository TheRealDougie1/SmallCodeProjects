"""
Basic Problem Summary:
    Given a list of people, create a list of random pairs.

    Example Input: ["Alex","Ben","Chris", "Dennis"]
    Example Output: {'Dennis': 'Ben', 'Chris': 'Alex'}

    Example Input: ["Alex","Ben","Chris","Dennis","Eve","Ffion","George","Harry"]
    Example Output: {'Ffion': 'Chris', 'Harry': 'George', 'Alex': 'Eve', 'Ben': 'Dennis'}

    Example Input: ["Alex","Ben","Chris","Dennis","Eve","Ffion","George"]
    Example Output: "Additional Name Required."

    Example Input: []
    Example Output: "Enter some names."

    Example Input: ["One Name"]
    Example Output: "Additional Name Required."
"""

import random

def PairAssigner(names: list):
    if len(names) == 0:
        return "Enter some names."
    if len(names) % 2 != 0:
        return "Additional Name Required."
    random.shuffle(names)
    subNamesPointer = int(len(names) / 2)
    firstGroupOfNames = names[0:subNamesPointer]
    secondGroupOfNames = names[subNamesPointer : len(names)]
    pairs = dict.fromkeys(firstGroupOfNames)
    for key in pairs:
        nameToAdd = secondGroupOfNames[0]
        pairs.update({key:nameToAdd})
        secondGroupOfNames.remove(nameToAdd)
    return pairs

if __name__ == "__main__":
    print(PairAssigner(["Alex","Ben","Chris","Dennis"]))
    print(PairAssigner(["Alex","Ben","Chris","Dennis","Eve","Ffion","George","Harry"]))
    print(PairAssigner(["Alex","Ben","Chris","Dennis","Eve","Ffion","George"]))
    print(PairAssigner([]))
    print(PairAssigner(["One Name"]))