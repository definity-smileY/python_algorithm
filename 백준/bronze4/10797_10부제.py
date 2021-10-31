a = int(input())
b = list(map(int, input().split()))

count = 0

for i in range(5):
    if a == b[i]:
        count += 1
print(count)