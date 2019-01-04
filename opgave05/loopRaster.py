#!/bin/python3

w=12
data=None
with open ("raster.txt", "r") as myfile:
    data=[[y for y in x.strip()] for x in myfile.readlines()]

def show(raster):
    print('\n'.join([' '.join(l) for l in raster]))

def makeForSubs(s):
    lst = [None] * 12
    for i in range(len(data)):
        lst[i] = [s[x] for x in data[i]]
    return lst

def spiral(w):
    r=0
    c=-1
    cl=w
    rl=w
    directions=[(0,1,0,-1),(1,0,-1,0),(0,-1,0,-1),(-1,0,-1,0)]
    i=0
    while i<w**2:
        for (dr,dc,drl,dcl) in directions:
            n= cl if dc == 0 else rl
            if n==0:
                break;
            for k in range(n):
                r+=dr
                c+=dc
                yield (r,c)
                i+=1
            rl+=drl
            cl+=dcl

def loopfinder():
    filled = makeForSubs({
        '<':'-','>':'+',
        'v':'[','n':']',
        'i':'.',
        'x':'>','-':'<'})

    print("filled")
    print("\nrows readout")
    s=""
    for r in range(w):
        for c in range(w):
            s+=filled[r][c]
    print(s)
    print("\ncols readout")
    s=""
    for c in range(w):
        for r in range(w):
            s+=filled[r][c]
    print(s)

    print("\nSpiral readout")
    s=""
    for (r,c) in spiral(w):
        s+=filled[r][c]
    print(s)


    print("\ntransposed spiral readout")
    s=""
    for (r,c) in spiral(w):
        s+=filled[c][r]
    print(s)





loopfinder()
