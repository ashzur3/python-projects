# -*- coding: utf-8 -*-
"""
Created on Fri May 21 16:57:05 2021

@author: yoshm
"""

import numpy as np
import random

GRID = np.array([[0,0,0, 3,0,4, 0,2,0],
                 [0,0,0, 2,0,5, 0,0,0],
                 [0,3,0, 0,0,0, 0,1,4],
                 
                 [3,2,0, 0,0,0, 0,9,7],
                 [0,0,0, 0,0,0, 3,0,0],
                 [8,4,0, 0,0,9, 2,6,0],
                 
                 [0,0,0, 0,5,2, 9,0,0],
                 [6,0,3, 8,0,1, 0,0,2],
                 [0,0,1, 4,0,0, 0,7,0]], dtype=int)

# sudoku int -> ndarray
def get_row(sudoku, y):
    return sudoku[y]

# sudoku int -> ndarray
def get_col(sudoku, x):
    return sudoku.T[x]

# sudoku int int -> ndarray
def get_block(sudoku, y, x):
    xr = x - x%3
    yr = y - y%3
    return sudoku[yr : yr+3, 
                  xr : xr+3]

ALL_NUM = { 1,2,3,4,5,6,7,8,9 }

# sudoku int int -> set of int
def allowed_numbers(sudoku, y, x):
    rs = set(get_row(sudoku, y))
    cs = set(get_col(sudoku, x))
    bs = set(get_block(sudoku, y, x).flat)
    vis = rs | cs | bs
    return ALL_NUM - vis



# sudoku ->
def solve(sudoku):
    (ey, ex) = np.where(sudoku == 0)
    empties = [ (ey[i], ex[i], allowed_numbers(sudoku, ey[i], ex[i])) for i in range(len(ey)) ]
    
    if len(empties) == 0:
        print(sudoku)
        return
    
    empties = sorted(empties, key=lambda x:len(x[2]))
    
    (y, x, allowed) = empties[0]
    
    if len(allowed) == 0:
        # incorrect digit
        return
    
    sudoku_copy = np.copy(sudoku)
    for digit in allowed:
        sudoku_copy[y, x] = digit
        solve(sudoku_copy)
        
        
solve(GRID)
    


    











