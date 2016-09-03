road = int(raw_input())  # the length of the road before the gap.
gap = int(raw_input())  # the length of the gap.
platform = int(raw_input())  # the length of the landing platform.

while True:
    speed = int(raw_input())  # the motorbike's speed.
    coord_x = int(raw_input())  # the position on the road of the motorbike.

    if coord_x > road:
        print "SLOW"
    elif (road-1 + gap) < (coord_x + speed):
        print "JUMP"
    else:
        if speed < gap + 1:
            print "SPEED"
        else:
            if speed != (gap + 1):
                print "SLOW"
            else:
                print "WAIT"
