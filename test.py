a = int(input()) # 방학 일수
b = int(input()) # 국어 페이지
c = int(input()) # 수학 페이지
d = int(input()) # 하루에 국어 최대 페이지
e = int(input()) # 하루에 수학 최대 페이지

if 2 <= a <= 40 and 1 <= b and c <= 1000 and 1 <= d and e <= 100:
    if b % d == 0:
        data_1 = b // d
    else:
        data_1 = b // d + 1    
    if c % e == 0:
        data_2 = c // e
    else:
        data_2 = c // e + 1
    
    max_date = max(data_1, data_2)
    print(a - max_date)
else:
    pass

