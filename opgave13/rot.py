#!/bin/python

import sys

alpha = list("abcdefghijklmnopqrstuvwxyz")

word = sys.argv[1]

l = len(alpha)

for rot in range(l):
    rotated = [alpha[(i + rot) % l] for i in range(l)]
    wordrot = [rotated[alpha.index(c)] for c in word]
    print("".join(wordrot) + " " + str(rot))

