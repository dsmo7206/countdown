#!/usr/bin/python

import sys
from itertools import groupby
from collections import defaultdict

FILES = ['brit-a-z.txt', 'britcaps.txt']

def makeCountMap(word):
    result = defaultdict(int)
    for letter in word:
        result[letter] += 1
    return result

WORD_MAP = dict(
    (word, makeCountMap(word))
    for word in (
        line.strip().lower()
        for fileName in FILES for line in open(fileName, 'r').xreadlines()
    )
    if word.isalpha()
)

def isInTarget(candidate, target):
    return all(
        target.get(letter, 0) >= count
        for letter, count in candidate.iteritems()
    )

def solve(target):
    targetMap = makeCountMap(target.lower())
    matches = sorted(
        (word for word, wcm in WORD_MAP.iteritems() if isInTarget(wcm, targetMap)),
        key=lambda m: len(m),
        reverse=True
    )
    if matches:
        wordLen, words = next(groupby(matches, lambda word: len(word)))
        return wordLen, list(words)
    else:
        return 0, []

def main():
    while True:
        target = sys.stdin.readline().strip()
        if not target.isalpha():
            break
        wordLen, words = solve(target)
        print('%s %s %s' % (wordLen, len(words), ' '.join(words)))

if __name__ == '__main__':
    main()
