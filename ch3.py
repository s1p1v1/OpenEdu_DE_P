#!/usr/bin/env python3
'''
x = float(input())
y = float(input())
print(x + y)


x = input()
try:
    y = x.split('.')[1]
    if y:
        print('0.' + y)
    else:
        print('0')
except:
    print('0')

x = float(input())
y = round(x%1, 5)
if y:
    print(y)
else:
    print(0)


x = float(input())
y = round(x)
if (not int(x)%2) and (x - int(x) == 0.5):  # x- четное
   y += 1
print(y)


p = int(input())
x = int(input())
y = int(input())

sv = 100 * x + y
print(sv)
sv += sv * p / 100
print(sv)
print('#'*10)
print(int(sv / 100), int(sv % 100))


s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[-1::-1])
print(s[-1::-2])
print(len(s))

s = input()
x = s.find('f')

if x != -1:
    y = s.rfind('f')
    if y != -1:
        if x != y:
            print(str(x),str(y))
        else:
            print(str(x))
    else:
        print(str(x))

s = input()
s1 = s.replace('A', 'B')
s2 = s1.replace('C', 'D')
print(s2)

s = input()
s1 = s.replace('A','*')
s2 = s1.replace('B','A')
s3 = s2.replace('*','B')
print(s3)

s = input()
ss = input()
if s.startswith(ss):
    print('True')
else:
    print('False')
'''
s = input()
print(s, len(s))
x = s.find('h')
s1 = s[:x+1]
print(x, s1, len(s1))
y = s.rfind('h')
s3 = s[y:]
print(y, s3, len(s3))
s2 = s[x+1:y].replace('h','H')
print(s2, len(s2))
print(s1+s2+s3)
'''
s = input()
ls = len(s)
if ls == 9:
    s1 = '+7' + s
elif ls == 10:
    s1 = '+7' + s[1:]
else:
    s1 = s
print(s1)
'''

