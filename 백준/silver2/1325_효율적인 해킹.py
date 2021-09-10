from collections import deque

N, M = map(int, input().split())

# 신뢰가가능 리스트
trust = [[] for _ in range(N + 1)]

count = [0] * (N + 1)

def BFS(node):
    q = deque()
    q.append(node)
    infected =  [False] * (N + 1)
    infected[node] = True
    
    while q:
        node = q.popleft()
        for nextNode in trust[node]:
            if infected[nextNode] == True:
                continue
            # 다음 노드넣은 후 방문 표시
            else:
                q.append(nextNode)
                infected[nextNode] = True
    
    return infected.count(True)

# 각 인덱스마다 신뢰하는 번호 넣기
for _ in range(M):
    dist, src = map(int, input().split())
    trust[src].append(dist)

for node in range(1, N + 1):
    count[node] = BFS(node)

for i in range(len(count)):
    if count[i] == max(count):
        print(i, end=" ")

"""
1 -> 3 -> 4 -> 5 : 4
2 -> 3 -> 4 -> 5 : 4
3 -> 4 -> 5 : 3
4 -> 5 : 2
5 : 1
"""