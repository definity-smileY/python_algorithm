"""
입력 값으로 키가 1인 사람부터 차례대로 자기보다 키가 큰 사람이 왼쪽에 몇명이 있었는지 주어지며, 줄을 선 순서대로 키를 출력하면 된다.

"""
n = int(input())
h = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):        
        if cnt == h[i] and result[j] == 0:
            result[j] = i + 1 # 수 1 ~ N
            break
        elif result[j] == 0:
            cnt += 1
print(*result)