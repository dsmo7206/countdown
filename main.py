from itertools import groupby
from collections import defaultdict

FILES = [
    'D:/Code/countdown/brit-a-z.txt',
    'D:/Code/countdown/britcaps.txt'
]

def makeCountMap(word):
    result = defaultdict(int)
    for letter in word:
        result[letter] += 1
    return result

def isInTarget(candidate, target):
    return all(
        target.get(letter, 0) >= count
        for letter, count in candidate.iteritems()
    )

def main():
    # Load words
    englishWordMap = dict(
        (word, makeCountMap(word))
        for word in (
            line.strip().lower()
            for fileName in FILES for line in open(fileName, 'r').xreadlines()
        )
        if word.isalpha()
    )

    while True:
        target = raw_input("Enter word ('q' to quit): ").lower()
        if not target.isalpha():
            print 'Invalid word. Try again...'
            continue
        if target == 'q':
            break
        targetMap = makeCountMap(target.lower())
        matches = sorted(
            (word for word, wcm in englishWordMap.iteritems() if isInTarget(wcm, targetMap)),
            key=lambda m: len(m),
            reverse=True
        )
        if matches:
            wordLen, words = next(groupby(matches, lambda word: len(word)))
            print 'Best result: %s letters\n\t%s' % (wordLen, list(words))
        else:
            print 'No matches.'

if __name__ == '__main__':
    main()

