# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the moutain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    max = 0
    m = 0
    for i in xrange(8):
        h = int(raw_input())  # represents the height of one mountain.
        if h > max:
            m = i
            max = h

    # The index of the mountain to fire on.
    print str(m)
