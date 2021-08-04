import sys

a, b, c, d = map(int, sys.stdin.readline().split())
aa, bb, cc, dd = map(int, sys.stdin.readline().split())

minguk = a + b + c + d
mansae = aa + bb + cc + dd

if minguk == mansae:
    print(minguk)
else:
    print(max(minguk, mansae))