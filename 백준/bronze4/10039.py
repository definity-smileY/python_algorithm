data = 0
for _ in range(5):
    a = int(input())
    if a < 40: data += 40
    else: data += a

print(data // 5)
