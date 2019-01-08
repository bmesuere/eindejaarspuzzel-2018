#!/bin/python

import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

mapping = {
 '.': False,
 'x': True,
 '-': None,
 'A': 1,
 'G': 2,
 'O': 3,
 'D': 4,
 'B': 5,
 'C': 6,
 'Z': 7
}

inverse = {
 'False': ' ',
 'True':  'x',
 'None':  '-'
}

def printBoard(b):
	print('\n'.join(''.join(inverse.get(str(c), str(c)) for c in row) for row in board))

board = [ [ mapping[c] for c in line.strip() ] for line in sys.stdin if line.strip() ]

rows = len(board)
cols = len(board[0])

deque = deque([(-1, board)])

def neighbours(r, c, rows, cols):
	return [ (r + dr, c + dc)
	         for dr in (-1, 0, 1)
	         for dc in (-1, 0, 1)
	         if r + dr in range(0, rows)
	         if c + dc in range(0, cols)
	       ]

depth = 0
while deque:
	i, board = deque.pop()
	if i > depth:
		print(i)
		depth = i

	i += 1
	while i < rows * cols and type(board[i // cols][i % cols]) is not int:
		i += 1
	if i >= rows * cols: break

	r, c = i // cols, i % cols
	bombs, nones = 0, []
	for r_, c_ in neighbours(r, c, rows, cols):
		if   board[r_][c_] is True: bombs += 1
		elif board[r_][c_] is None: nones.append((r_, c_))
	if bombs > board[r][c]: continue
	if bombs + len(nones) < board[r][c]: continue

	for selected in combinations(nones, board[r][c] - bombs):
		copy = deepcopy(board)
		for r_, c_ in nones:
			copy[r_][c_] = (r_, c_) in selected
		deque.append((i, copy))

printBoard(board)
