# import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]

tx = initial_tx
ty = initial_ty
lx = light_x
ly = light_y

# game loop
while True:
    remaining_turns = int(raw_input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # A single line providing the move to be made: N NE E SE S SW W or NW
    if ty < ly:
        ty += 1
        if tx < lx:
            print "SE"
            tx += 1
            continue
        if tx > lx:
            print "SW"
            tx -= 1
            continue
        print "S"
        continue
    elif ty > ly:
        ty -= 1
        if tx < lx:
            print "NE"
            tx += 1
            continue
        if tx > lx:
            print "NW"
            tx -= 1
            continue
        print "N"
        continue
    if tx < lx:
        print "E"
        tx += 1
    else:
        print "W"
        tx -= 1
