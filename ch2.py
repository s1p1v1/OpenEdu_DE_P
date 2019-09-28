#!/usr/bin/env python3

'''
x = int(input())
y = (6 <= x <= 8) or (16 <= x <= 17)
print(y)

A = int(input())
B = int(input())
C = int(input())
D = int(input())
x = int(input())
y = (A <= x <= B) and not(C <= x <= D)
print(y)

x = int(input())
y = x % 3 == 1 and x % 4 == 1
print(y)

x = int(input())
y = int(input())
z = int(input())
if x>y:
    if x>z:
        print(x)
    else:
        print(z)
elif y>z:
    print(y)
else:
    print(z)

#год является високосным
x = int(input())
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print('YES')
else:
    print('NO')

# хотя бы одно четное и хотя бы одно нечетное
x = int(input())
y = int(input())
z = int(input())
x1 = x % 2 == 0
y1 = y % 2 == 0
z1 = z % 2 == 0
if (x1 or y1 or z1) and (not x1 or not y1 or not z1):
    print('YES')
else:
    print('NO')

n = int(input())
x = 1
while x**2 <= n:
    print(x, x**2)
    x += 1

n = int(input())
x = 0
while 2**x <= n:
    print(2**x, end=' ')
    x += 1

n = int(input())
n1 = n
count = 0
while n:
    if n > n1:
        count += 1
    n1 = n
    n = int(input())
print(count)

n = int(input())
max = 0
count = 0
while n:
    if n > max:
        max = n
        count = 1
    elif n == max:
        count += 1
    n = int(input())
print(count)

n = int(input())
count = 0
i = 1
while i <= n:
    k = int(input())
    if not k:
        count += 1
    i += 1
print(count)

n = int(input())
i = 1
k = str(i)
while i <= n:
    print(k)
    i += 1
    k += str(i)
'''
x = int(input())
y = int(input())
while x <= y:
    print(x, end=' ')
    x += 1

