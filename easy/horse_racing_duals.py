n = int(raw_input())

horses = [int(raw_input()) for _ in xrange(n)]

horses.sort()

m = 10000000

for i in xrange(n - 1):
    c = horses[i+1] - horses[i]
    if c < m:
        m = c

print(m)
