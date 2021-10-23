# result output like:
#
#      apples Alice dogs 
#     oranges Bob   cats
#    cherries Carol moose
#      banana David goose
#

import math

tableData =[
    ['apples', 'oranges', 'cherries', 'banana']
    ,['Alice', 'Bob', 'Carol', 'David']
    ,['dogs', 'cats', 'moose', 'goose']
    ]

len_inner_pre_max = 0
len_outter_pre = len(tableData)
maxWidth = {}

for i in range(len_outter_pre):
    if len_inner_pre_max < len(tableData[i]):
        len_inner_pre_max = len(tableData[i])
    tempMaxWidth = 0
    for j in range(len_inner_pre_max):
        if tempMaxWidth < len(tableData[i][j]):
            tempMaxWidth = len(tableData[i][j])
    maxWidth[i] = tempMaxWidth

for m in range(len_inner_pre_max):
    for n in range(len_outter_pre):
        if n == 0:
            print(tableData[n][m].rjust(maxWidth[n]), end="")
        elif n == len_outter_pre - 1:
            print(tableData[n][m].ljust(maxWidth[n]))
        else:
            print(tableData[n][m].center(maxWidth[n] + 2), end="")