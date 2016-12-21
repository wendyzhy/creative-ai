#!/usr/bin/env python
import random
from collections import Counter
from data.dataLoader import *

def total(text):
    pass

def prep(text):
    return (['^::^', '^:::^'] + line + ['$::$'] for line in text)

def ngrams(line, n):
    return zip(*[line[i:] for i in range(n)])

if __name__ == "__main__":
    pass
