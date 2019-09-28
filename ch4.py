#!/usr/bin/env python3
'''
str = input()
lis = list(map(int,str.strip().split()))
#print(lis)
max = lis[0]
j = 0
for i in range(0,len(lis)):
    l1 = lis[i]
    if l1 > max:
        max = l1
        j = i

print(max, j)


j = 0
for i in range(0, len(lis)):
    l1 = int(lis[i])
    if l1 > max:
        max = l1
        j = i

print(max, j)

str = input()
lis = map(int, str.strip().split())
#print(lis)
min = 10000
for i in lis:
    l1 = int(i)
    if l1 < min and l1 > 0:
        min = l1

print(min)


def min(l):
    ml = l[0]
    j = 0
    for i in range(0, len(l)):
        li = l[i]
        if li < ml:
            ml = li
            j = i
    return (ml, j)

def max(l):
    ml = l[0]
    j = 0
    for i in range(0, len(l)):
        li = l[i]
        if li > ml:
            ml = li
            j = i
    return (ml, j)

l = list(map(int, input().strip().split()))
m1 = min(l)
print(m1)
m2 = max(l)
print(m2)
l[m1[1]] = str(m2[0])
l[m2[1]] = str(m1[0])
l = list(map(str, l))
print(' '.join(l))

def xor(x=1, y=1):
    return int(x and not y or not x and y)

print(xor(1,1))
print(xor(0,1))
print(xor(0,0))
print(xor(1,0))

def isPointInSquare(x, y):
    return abs(x) <= 1 and abs(y) <= 1

x = float(input())
y = float(input())
if isPointInSquare(x, y):
    print('YES')
else:
    print('NO')
'''
def sort3(a,b,c):
    if a > b:
        if b > c:
            return c,b,a
        elif a > c:
            return b,c,a
        else:
            return b,a,c
    else:
        if a > c:
            return c,a,b
        elif b > c:
            return a,c,b
        else:
            return a,b,c

x = int(input())
y = int(input())
z = int(input())
print(' '.join(list(map(str,sort3(x,y,z)))))
