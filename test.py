a, b = map(int, input().split())
c = int(input())

minnit = b + c

if minnit >= 59:
    hour = minnit // 60
    mm = minnit % 60

    hour_sum = a + hour 
    print(hour_sum, mm)
    if hour_sum >= 24:
        hour_sum = 0
        print(hour_sum, mm)

    # else:
    #     print(hour_sum, minnit)