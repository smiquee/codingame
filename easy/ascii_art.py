# import sys

l = int(raw_input())
h = int(raw_input())
t = raw_input()

# Init letters
letters = dict()

for i in xrange(ord('a'), ord('z') + 1):
    letters[chr(i)] = [''] * h

letters['?'] = [''] * h

for i in xrange(h):
    row = raw_input()
    j = 0
    for letter in xrange(ord('a'), ord('z') + 1):
        letters[chr(letter)][i] = row[j:j+l]
        j += l
    letters['?'][i] = row[j:j+l]

for c in xrange(h):
    out = ""
    for letter in t:
        try:
            out += letters[letter.lower()][c]
        except KeyError:
            out += letters['?'][c]
    print(out)


# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
