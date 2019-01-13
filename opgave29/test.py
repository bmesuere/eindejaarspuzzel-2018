#!/bin/python

def mkTable(fromList,toList):
    table = {ord(i[0]): ord(i[1]) for i in zip(fromList, toList)}
    def rot(s,times=1):
        ret = s;
        for i in range(times):
            ret = ret.translate(table)
        return ret
    return rot

deg45 = mkTable("abcdefghijklmnopqrstuvwxyz#-","hiklmnaopxqrsbtuy-c#jezfvgwd")
behind = mkTable("#-zyxwvutsrqponmlkjihgfedcba","tlhqioku#mryjwns-vpxzabcdefg")


a ="""hmwqkyzx
otdtluzn
e#rl#wno
emiujqhu
eesldgal"""
a=a.split("\n")


print("45 deg rotations")
for r in range(len(a)):
    s=""
    for d in range(8):
        s+="  "
        for c in range(len(a[r])):
            s+=deg45(a[r][c],r+d)
    print(s)

print("\nalternating behind")
for r in a:
    s=r + "  " + deg45(behind(r)) + "   "
    s+=""
    for i in range(len(r)):
        s+=deg45(behind(r[i],i))
    s+="   "
    for i in range(len(r)):
        s+=behind(deg45(r[i],4))

    print(s)
