data = [int(input()) for _ in range(3)]

if sum(data) == 180:
    if data[0] == data[1] == data[2] == 60: print("Equilateral")
    elif data[0] == data[1] or data[0] == data[2] or data[1] == data[2]: print("Isosceles")
    else: print("Scalene")
else: print("Error")
