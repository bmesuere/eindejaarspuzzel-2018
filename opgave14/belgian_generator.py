digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

class Number:

    def __init__(self, value, base):
        self.base = base
        if isinstance(value, str):
            self.content = []
            for element in value:
                self.content.append(digits.index(element))
            self.content = self.content[::-1]
        else:
            self.content = value

    def __str__(self):
        lijst = []
        for digit in self.content:
            lijst.append(digits[digit])
        return ''.join(lijst[::-1])

    def __add__(self, other):
        assert other.base == self.base, 'different base'
        newcontent = self.content[:]
        carry = 0
        for index, digit in enumerate(other.content):
            toadd = carry + digit
            carry = 1 if newcontent[index] + toadd >= self.base else 0
            if index == len(self.content):
                newcontent.append(0)
            newcontent[index] = (newcontent[index] + toadd) % self.base

        while carry:
            index += 1
            if index == len(self.content):
                newcontent.append(1)
                carry = 0
            else:
                carry = 1 if newcontent[index] + 1 >= self.base else 0
                newcontent[index] = (newcontent[index] + 1) % self.base

        return Number(newcontent, self.base)

    def __lt__(self, other):
        if len(self.content) < len(other.content):
            return True
        elif len(self.content) > len(other.content):
            return False
        else:
            index = -1
            while index >= -len(self.content) and self.content[index] == other.content[index]:
                index -= 1
            return index >= -len(self.content) and self.content[index] < other.content[index]

    def __eq__(self, other):
        return self.content == other.content

def convert(decimal, base):
    if decimal < base:
        return digits[decimal]
    else:
        res = decimal % base
        return convert(decimal//base, base) + digits[res]

def isBelgianNumber(number, base = 10):
    #nummer naar nieuwe basis omzetten
    geconverteerd = convert(number, base)
    
    digits = [Number(teken, base) for teken in geconverteerd]
    number = Number(geconverteerd, base)

    som = Number('0', base)
    digitindex = 0
    while som < number:
        som += digits[digitindex]
        digitindex = (digitindex + 1) % len(digits)

    return som == number

def belgianNumbers(complement = False, base = 10):
    current = 0
    while True:
        if (not complement and isBelgianNumber(current, base)) or \
        (complement and not isBelgianNumber(current, base)):
            yield current
        current += 1

import itertools
import sys

aantal = 30


base = int(sys.argv[1])

belgians = itertools.islice(belgianNumbers(base = base), aantal)
nonbelgians = itertools.islice(belgianNumbers(complement = True, base = base), aantal)
print(' '.join(str(item) for item in belgians))
print(' '.join(str(item) for item in nonbelgians))
