n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed.

tab = dict()

for i in xrange(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = raw_input().split()
    tab[ext.lower()] = mt

for i in xrange(q):
    fname = raw_input()  # One file name per line.
    try:
        name, ext = fname.rsplit('.', 1)
    except ValueError:
        print("UNKNOWN")
        continue
    print(tab.get(ext.lower(), "UNKNOWN"))
