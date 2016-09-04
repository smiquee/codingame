n = int(raw_input())  # the number of points used to draw the surface of Mars.

land_x = [-1] * n
land_y = [-1] * n

for i in xrange(n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x[i], land_y[i] = [int(j) for j in raw_input().split()]

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in raw_input().split()]

    if abs(v_speed) > 40 :
        power = power + 1 if power < 4 else 4
        print "0 %d" % power
    else:
        power = power - 1 if power > 2 else 2
        print "0 %d" % power
