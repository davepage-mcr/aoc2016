#!/usr/bin/python

# Initial startup

import sys

keypad = [
            [ None, None, '1', None, None ],
            [ None, '2',  '3', '4',  None ],
            [ '5',  '6',  '7', '8',  '9'  ],
            [ None, 'A',  'B', 'C',  None ],
            [ None, None, 'D', None, None ],
         ]
coords = [ 2, 0 ]

code = ''

inputfile = open(sys.argv[1])

for line in inputfile:
  coordstring = ','.join(map(str,coords))

  print "Starting at " + coordstring + " pad " + str(keypad[coords[0]][coords[1]])
  print "Following " + line

  for step in line:

    if step == 'R':
        if coords[1] < 4 and keypad[coords[0]][coords[1]+1] != None:
            coords[1] += 1
    elif step == 'D':
        if coords[0] < 4 and keypad[coords[0]+1][coords[1]] != None:
            coords[0] += 1
    elif step == 'L':
        if coords[1] > 0 and keypad[coords[0]][coords[1]-1] != None:
            coords[1] -= 1
    elif step == 'U':
        if coords[0] > 0 and keypad[coords[0]-1][coords[1]] != None:
            coords[0] -= 1

  coordstring = ','.join(map(str,coords))
  print "Now at " + coordstring + " pad " + str(keypad[coords[0]][coords[1]])

  code += str(keypad[coords[0]][coords[1]])

print "Door code is " + code
