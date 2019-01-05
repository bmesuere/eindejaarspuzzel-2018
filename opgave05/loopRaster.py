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

def diagonal(w):
    for i in range(w):
        pos = (0,i)
        yield pos
        for j in range(i):
            yield (pos[0]+1+j,pos[1]-1-j)
    for i in range(w-1):
        pos = (i+1,w-1)
        yield pos
        for j in range(w-i-2):
            yield (pos[0]+1+j,pos[1]-1-j)



def loopfinder(s):
    filled = makeForSubs(s)
    print("---------------")
    print(f"filled {s}")
    show(filled)
    print("\nrows readout")
    s=""
    for r in range(w):
        for c in range(w):
            s+=filled[r][c]
    print(s)
    print("\nrows readout RTL")
    s=""
    for r in range(w):
        for c in range(w):
            s+=filled[r][w-c-1]
    print(s)
    print("\ncols readout")
    s=""
    for c in range(w):
        for r in range(w):
            s+=filled[r][c]
    print(s)

    print("\ncols readout down to up")
    s=""
    for c in range(w):
        for r in range(w):
            s+=filled[w-r-1][c]
    print(s)

    print("\ncols readout right to left")
    s=""
    for c in range(w):
        for r in range(w):
            s+=filled[r][w-c-1]
    print(s)

    print("\ncols readout down to up and right to left")
    s=""
    for c in range(w):
        for r in range(w):
            s+=filled[w-r-1][w-c-1]
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


    print("\ndiagonal readout")
    s=""
    for (r,c) in diagonal(w):
        s+=filled[r][c]
    print(s)


    print("\ntransposed diagonal readout")
    s=""
    for (r,c) in diagonal(w):
        s+=filled[c][r]
    print(s)


# make a dict that maps the chars of "<>vnix-"
def t(s):
    return dict([("<>vnix-"[i],v) for i,v in enumerate(s)])

#            "<>vnix-"
loopfinder(t("<>[].+-"))
loopfinder(t("<>[]+.-"))
loopfinder(t("-+[].><"))
