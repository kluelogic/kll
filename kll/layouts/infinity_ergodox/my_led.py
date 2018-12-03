#!/usr/bin/env python3
#
# my_led.py
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

taper_off_snake = True

snake_path = [ 29, 20, 14, 7,
               6, 13, 19, 28, 37,
               36, 27, 18, 12, 5,
               4, 11, 17, 26, 35,
               34, 25, 16, 10, 3,
               2, 9, 15, 24,
               33, 32, 31, 30, 21, 22,
               23, 8, 1, # top right
               2, 3, 4, 5, 6, 7,
               14, 13, 12, 11, 10, 9, 8,
               15, 16, 17, 18, 19, 20,
               29, 28, 27, 26, 25, 24, 23,
               22, 21, 30, 31, 32, 33,
               34, 35, 36, 37 ]

if taper_off_snake: snake_path.insert( 0, 38 )
else:               snake_path.append( 38 )

def print_snake( frame, path, head_pos, snake_length ):
    print( 'A[snake, {}] <= '.format( frame ), end = '' )
    tail_pos = head_pos - snake_length
    print( 'P[{}](0),'.format( path[ tail_pos ] ), end = '' )
    print( 'P[{}](255);'.format( path[ head_pos ] ) )

def snake_dies_out( frame ):
    for length in range( snake_length, 0, -1 ):
        print_snake( frame, snake_path, 0, length )
        frame += 1
    print( 'A[snake, {}] <= P[{}](0);'.format( frame, snake_path[0] ) )
    
# main

frame = 1
snake_length = 7
for head_pos in range( len( snake_path ) ): # run a snake
    print_snake( frame, snake_path, head_pos, snake_length )
    frame += 1

if taper_off_snake: snake_dies_out( frame )

