# import sys

n = int(raw_input())  # the number of temperatures to analyse
temps = raw_input().split(' ')  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

if n == 0:
    print(0)
else:
    closer = int(temps[0])

    for i in xrange(1, n):
        if closer == 0:
            break
        if abs(int(temps[i])) < abs(closer):
            closer = int(temps[i])
            continue
        if abs(closer) == abs(int(temps[i])):
            if int(temps[i]) > 0:
                closer = int(temps[i])

    print(closer)
