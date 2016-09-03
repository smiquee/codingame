n = int(raw_input())
chars = raw_input().split()[0:n]

res = [''] * n

pos = 0
neg = False
fl = False

if '-' in chars:
    res[pos] = '-'
    pos += 1
    neg = True

if '.' in chars:
    fl = True
    if pos != 0:
        res[2] = '.'
    else:
        res[-2] = '.'

ints = list()
for c in chars:
    if c != '-' and c != '.':
        ints.append(int(c))

if '-' in chars:
    ints.sort()
else:
    ints.sort(reverse=True)

if neg and ints[-1] == 0:
    print '0'
else:
    for i in ints:
        while res[pos] != '':
            pos += 1
        res[pos] = str(i)

    if fl:
        if not neg and res[-1] == '0':
            res = res[:-2]

    if '.' in res:
        print float(''.join(res))
    else:
        print int(''.join(res))
