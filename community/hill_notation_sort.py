# Define some lists
lowers = [chr(x) for x in xrange(ord('a'), ord('z') + 1)]
uppers = [chr(x) for x in xrange(ord('A'), ord('Z') + 1)]
ints = [str(n) for n in xrange(10)]


# Define some functions
def expand(s):
    if '(' not in s:
        return s

    ns = ""
    paren = False
    mul = ""
    i = 0
    elt = ""

    while i < len(s):
        if not paren and s[i] != '(':
            ns += s[i]
            i += 1
        else:
            if s[i] == '(':
                paren = True
            elif s[i] == ')':
                i += 1
                mul = ""
                while i < len(s) and s[i] in ints:
                    mul += s[i]
                    i += 1
                i -= 1
                if len(mul) == 0:
                    mul = '1'
                nb = int(mul)
                ns += nb * elt
                paren = False
                elt = ""
                mul = ""
            else:
                elt += s[i]
            i += 1

    return ns


def arrange(s):
    s = expand(s)
    d = dict()
    i = 0
    while i < len(s):
        elt = s[i]
        i += 1
        nb = ""
        while i < len(s) and s[i] in lowers:
            elt += s[i]
            i += 1
        while i < len(s) and s[i] in ints:
            nb += s[i]
            i += 1
        if len(nb) == 0:
            n = 1
        else:
            n = int(nb)
        if elt in d:
            d[elt] += n
        else:
            d[elt] = n

    return d


def show(d):
    res = ""
    sd = sorted(d)

    if 'C' in sd:
        res += "C"
        if d['C'] > 1:
            res += "%d" % d['C']
        if 'H' in sd:
            res += "H"
            if d['H'] > 1:
                res += "%d" % d['H']
        for elt in sd:
            if elt != 'C' and elt != 'H':
                res += elt
                if d[elt] > 1:
                    res += "%d" % d[elt]
    else:
        for elt in sd:
            res += elt
            if d[elt] > 1:
                res += "%d" % d[elt]
    return res


def sort_elt(l):
    res = list()
    r = sorted(l)

    if 'C' in r:
        res.append('C')
        if 'H' in r:
            res.append('H')
        for elt in r:
            if elt != 'C' and elt != 'H':
                res.append(elt)
        return res
    return r


def inf(d1, d2):
    m = min(len(d1), len(d2))

    sd1 = sort_elt(d1.keys())
    sd2 = sort_elt(d2.keys())

    for i in xrange(m):
        if sd1[i] < sd2[i]:
            return True
        if sd1[i] > sd2[i]:
            return False
        if sd2[i] == sd1[i]:
            if d1[sd1[i]] < d2[sd2[i]]:
                return True
            if d1[sd1[i]] > d2[sd2[i]]:
                return False


def insert(l, elt):
    found = False
    for i in xrange(len(l)):
        if inf(elt, l[i]):
            l.insert(i, elt)
            found = True
            break
    if not found:
        l.append(elt)


# Play with inputs
num_compounds = int(raw_input())
compounds = list()

for i in xrange(num_compounds):
    compounds.append(raw_input())

r = list()

for e in compounds:
    insert(r, arrange(e))

tmp = [show(e) for e in r]

res = list()
for elt in tmp:
    if elt not in res:
        res.append(elt)

for elt in res:
    print elt
