#!/bin/python3
# Name:
# By Robbert Gurdeep Singh
################################################################################

def belArr(b,i): # real
    parts = list(map(int,str(i)));
    ret = [b];
    while ret[-1] < i:
        for p in parts:
            if ret[-1] < i:
                ret.append(ret[-1] + p)
    return ret

def belArr2(b,i): # test
    parts = list(map(int,str(i)));
    for j  in list(map(int,str(b))):
        parts.append(j)
    ret = [0];
    while ret[-1] < i:
        for p in parts:
            if ret[-1] < i:
                ret.append(ret[-1] + p)
    return ret


for i in range(50):
    steps=belArr(3,i)
    print(i, steps[-1]-i, len(steps), steps );
