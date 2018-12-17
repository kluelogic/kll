#!/usr/bin/env python3
#
# tatejima.py
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

tatejima_list = [ [        21, 22, 30, 31 ],
                  [ 1,  8,     23, 32, 33 ],
                  [ 2,  9, 15, 24 ],
                  [ 3, 10, 16, 25, 34 ],
                  [ 4, 11, 17, 26, 35 ],
                  [ 5, 12, 18, 27, 36 ],
                  [ 6, 13, 19, 28, 37 ],
                  [ 7, 14, 20, 29, 38 ] ]
                  
def print_tatejima():
    for i, on_list in enumerate( tatejima_list ):
        frame      = 'A[tatejima, {}] <= '.format( i + 1 )
        on_pixels  = ','.join( [ 'P[{}](255)'.format( p ) for p in on_list ] )
        off_list   = tatejima_list[ i - 1 ] # if i == 0 then use the last entry of tatejima_list (i.e. tatejima_list[-1])
        off_pixels = ','.join( [ 'P[{}](0)'.format( p ) for p in off_list ] )
        print( frame + on_pixels + ',' + off_pixels + ';' )

# main

print_tatejima()
