#!/usr/bin/env python3
import string
import unicodedata


def normalize(s):
    nkfd_form = unicodedata.normalize('NFKD', s)
    return "".join([c.lower() for c in nkfd_form if not unicodedata.combining(c)])


with open("../woordenlijst.txt", encoding='latin-1') as f:
    wordlist = [normalize(w.strip()) for w in f]

words = ["ben", "gelijk", "hal", "koek", "meed", "pers", "wend"]


def is_missing(word, letter, w):
    return letter in w \
        and len(w) == len(word) + 1 \
        and sorted(w.replace(letter, "")) == sorted(word)


def solutions(word, letter):
    return [w for w in wordlist if is_missing(word, letter, w)]


for letter in string.ascii_lowercase:
    solution = [solutions(word, letter) for word in words]
    if all(solution):
        print(letter, solution)
