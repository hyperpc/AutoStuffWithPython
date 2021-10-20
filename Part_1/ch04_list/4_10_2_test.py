# result output like:
#
#   ..oo.oo..
#   .ooooooo.
#   .ooooooo.
#   ..ooooo..
#   ...ooo...
#   ....o....
#

import math


grid =[
    ['.', '.', '.', '.', '.', '.']
    ,['.', 'o', 'o', '.', '.', '.']
    ,['o', 'o', 'o', 'o', '.', '.']
    ,['o', 'o', 'o', 'o', 'o', '.']
    ,['.', 'o', 'o', 'o', 'o', 'o']
    ,['o', 'o', 'o', 'o', 'o', '.']
    ,['o', 'o', 'o', 'o', '.', '.']
    ,['.', 'o', 'o', '.', '.', '.']
    ,['.', '.', '.', '.', '.', '.']
    ]

len_inner_pre_max = 0
len_outter_pre = len(grid)

for i in range(len_outter_pre):
    if len_inner_pre_max < len(grid[i]):
        len_inner_pre_max = len(grid[i])

for m in range(len_inner_pre_max):
    for n in range(len_outter_pre):
        if n == len_outter_pre - 1:
            print(grid[n][m])
        else:
            print(grid[n][m], end="")