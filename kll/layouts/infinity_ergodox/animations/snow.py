#!/usr/bin/env python3
#
# snow.py
#

# Pixel Position:
#
# P[ 7] P[ 6] P[ 5] P[ 4] P[ 3] P[ 2] P[ 1]
# P[14] P[13] P[12] P[11] P[10] P[ 9] P[ 8]
# P[20] P[19] P[18] P[17] P[16] P[15]
# P[29] P[28] P[27] P[26] P[25] P[24] P[23]
# P[38] P[37] P[36] P[35] P[34]             P[22] P[21]
#                                                 P[30]
#                                     P[33] P[32] P[31]

import random

board = [ [ 1, 8,   23 ],
          [ 2, 9,15,24 ],
          [ 3,10,16,25,34 ],
          [ 4,11,17,26,35 ],
          [ 5,12,18,27,36 ],
          [ 6,13,19,28,37 ],
          [ 7,14,20,29,38 ] ]

snow= [ [ 0,0,0 ],
        [ 0,0,0,0 ],
        [ 0,0,0,0,0 ],
        [ 0,0,0,0,0 ],
        [ 0,0,0,0,0 ],
        [ 0,0,0,0,0 ],
        [ 0,0,0,0,0 ] ] # initial

def random_bool( probability ):
    return random.randint( 0, 100 ) < probability # randint generates a number between 0 and 100

def find_gap_from_the_bottom( path ):
    for i in range( len( path ) - 1, 0, -1 ):
        if path[i] == 0: return i # found gap
    return -1

def snow_fall( appear_prob, disappear_prob ):
    for i, path in enumerate( snow ):
        if path[-1] == 1: # snow at the bottom
            if random_bool( disappear_prob ): path[-1] = 0 # randomly remove the snow at the bottom
        gap_pos = find_gap_from_the_bottom( path )
        if gap_pos >= 0:
            if random_bool( appear_prob ): val = 1
            else:                          val = 0
            snow[i] = [ val ] + path[:gap_pos] + path[gap_pos + 1:] # remove gap
                  
def print_snow( num_frames, appear_prob, disappear_prob ):
    for frame in range( num_frames ):
        if frame == 0:
            print( 'A[snow, 1] <= P[r:0](0),P[r:1](0),P[r:2](0),P[r:3](0),P[r:4](0),P[r:5](0),P[r:6](0);' )
            continue
        old_snow = snow.copy()
        snow_fall( appear_prob, disappear_prob )
        changes = []
        for i, path in enumerate( snow ):
            for j, p in enumerate( path ):
                if snow[i][j] != old_snow[i][j]:
                    if snow[i][j] == 1: val = 255
                    else:               val = 0
                    changes.append( ( board[i][j], val ) )
        if len( changes ) == 0: continue
        pixels = ','.join( [ 'P[{}]({})'.format( change[0], change[1] ) for change in changes ] )
        print( '#', snow )
        print( 'A[snow, {}] <= {};'.format( frame + 1, pixels ) )

# main

num_frames     = 50
appear_prob    = 20
disappear_prob = 20
print_snow( num_frames, appear_prob, disappear_prob )
