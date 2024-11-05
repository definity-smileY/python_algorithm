import sys

for _ in range(3):
    hh, mm, ss, hhh, mmm, sss= map(int, sys.stdin.readline().split())
    
    t1 = hh * 60 * 60 + mm * 60 + ss
    t2 = hhh * 60 * 60 + mmm * 60 + sss
    t = t2 - t1
    h = t // 60 // 60 % 24
    m = t // 60 % 60
    s = t % 60

    print(h, m, s)