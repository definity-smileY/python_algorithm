import sys

sum = []
for _ in range(5):
    data = int(sys.stdin.readline())
    sum.append(data)
burger = sum[0:3]
dring = sum[3:]
print(min(burger) + min(dring) - 50)

