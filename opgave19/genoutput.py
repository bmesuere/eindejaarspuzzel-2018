f = open('board.txt')
board = f.readlines()
f.close()
f = open('mines.txt')
mines = f.readlines()
out = ""

colormap = {
        '-': '\033[47m -',
        'M': '\033[40m M',
        '1': '\033[104m 1',
        '2': '\033[42m 2',
        '3': '\033[43m 3',
        '4': '\033[44m 4',
        '5': '\033[100m 5',
        '6': '\033[106m 6',
        '7': '\033[40m 7',
}
for x in range(33):
 for y in range(32):
  if int(mines[x][y]):
    out +=colormap['M']
  else:
   out +=colormap[board[x][y]]
 out += '\n'

print out
