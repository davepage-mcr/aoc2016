#!/usr/bin/python

# Initial startup

headings = [ 'north', 'east', 'south', 'west' ]
heading=0

input="R2, L3"
input="R2, R2, R2"
input="R5, L5, R5, R3"
input="L1, R3, R1, L5, L2, L5, R4, L2, R2, R2, L2, R1, L5, R3, L4, L1, L2, R3, R5, L2, R5, L1, R2, L5, R4, R2, R2, L1, L1, R1, L3, L1, R1, L3, R5, R3, R3, L4, R4, L2, L4, R1, R1, L193, R2, L1, R54, R1, L1, R71, L4, R3, R191, R3, R2, L4, R3, R2, L2, L4, L5, R4, R1, L2, L2, L3, L2, L1, R4, R1, R5, R3, L5, R3, R4, L2, R3, L1, L3, L3, L5, L1, L3, L3, L1, R3, L3, L2, R1, L3, L1, R5, R4, R3, R2, R3, L1, L2, R4, L3, R1, L1, L1, R5, R2, R4, R5, L1, L1, R1, L2, L4, R3, L1, L3, R5, R4, R3, R3, L2, R2, L1, R4, R2, L3, L4, L2, R2, R2, L4, R3, R5, L2, R2, R4, R5, L2, L3, L2, R5, L4, L2, R3, L5, R2, L1, R1, R3, R3, L5, L2, L2, R5"

coords = [0,0]

instructions = input.split(", ")
for instruction in instructions:
    turn = instruction[0]
    dist = int(instruction[1:])

    print "Instruction: turn " + turn + " and walk " + str(dist) + " blocks"

    if turn == "L":
        heading = ( heading - 1 ) % 4
    elif turn == "R":
        heading = ( heading + 1 ) % 4
    else:
        print "Illegal turn instruction: " + turn
        continue

    print "Moving " + str(dist) + " blocks " + headings[heading]

    if heading == 0:
        coords[1] += dist
    elif heading == 1:
        coords[0] += dist
    elif heading == 2:
        coords[1] -= dist
    elif heading == 3:
        coords[0] -= dist
    else:
        print "Illegal heading " + str(heading)

    coordstring = ','.join(map(str,coords))

    print "At " + coordstring + " facing " + headings[heading]


print "We are " + str(abs(coords[0]) + abs(coords[1])) + " blocks from start"
