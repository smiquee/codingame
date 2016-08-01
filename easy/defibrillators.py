import math

lon = raw_input().replace(',', '.')
lat = raw_input().replace(',', '.')
n = int(raw_input())

dest = ""
d = -1

for i in xrange(n):
    defib = raw_input().replace(',', '.').split(';')
    dd = math.sqrt(math.pow((float(lon) - float(defib[4])) *
                             math.cos((float(defib[4]) + float(lon))/2),2) +
                   math.pow(float(lat) - float(defib[5]),2)) * 6371
    if d == -1 or dd < d:
        dest = defib[1]
        d = dd

print dest
