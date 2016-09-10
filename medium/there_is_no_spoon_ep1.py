# Don't let the machines win. You are humanity's last hope...

width = int(raw_input())  # the number of cells on the X axis
height = int(raw_input())  # the number of cells on the Y axis

grid = list()

for i in xrange(height):
    grid.append(list(raw_input()))  # width characters, each either 0 or .

# Three coordinates: a node, its right neighbor, its bottom neighbor
for i in xrange(height):
    for j in xrange(width):
        res = ""
        right = False
        bottom = False
        if grid[i][j] != '.':
            res = '%d %d' % (j, i)
            for n in xrange(j+1, width):
                if grid[i][n] != '.':
                    res += ' %d %d' % (n, i)
                    right = True
                    break
            if not right:
                res += ' -1 -1'

            for m in xrange(i+1, height):
                if grid[m][j] != '.':
                    res += ' %d %d' % (j, m)
                    bottom = True
                    break
            if not bottom:
                res += ' -1 -1'

            print res
