#!/usr/bin/env python3
#
# checker.py
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

checker_list = [ [ 7, 5, 3,  1, 13, 11, 9, 20, 18, 16, 28, 26, 24, 23, 21, 38, 36, 34, 32, 31 ],
                 [ 6, 4, 2, 14, 12, 10, 8, 19, 17, 15, 29, 27, 25, 22,     37, 35, 33,     30 ] ]

def print_checker( delta ):
    on_pixels  = ','.join( [ 'P[{}](+{})'.format( p, delta ) for p in checker_list[0] ] )
    off_pixels = ','.join( [ 'P[{}](-{})'.format( p, delta ) for p in checker_list[1] ] )
    print( 'A[checker, 1] <= ' + on_pixels + ',' + off_pixels + ';' )
    # on_pixels  = ','.join( [ 'P[{}]()'.format( p ) for p in checker_list[1] ] )
    # off_pixels = ','.join( [ 'P[{}](18)'.format( p ) for p in checker_list[0] ] )
    # print( 'A[checker, 2] <= ' + on_pixels + ',' + off_pixels + ';' )

# main

print_checker( delta = 32 )
