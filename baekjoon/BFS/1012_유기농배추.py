import sys
from collections import deque
"""
1. 너비 우선 탐색 풀이
2. 2차원 배열의 유기농 배추밭이 주어지고 0과 1로 데이터 구분
3. 배추흰 지렁이를 배추에 서식하게 하면 사방면으로 이동이 가능
4. 필요한 배추흰 지렁이의 마리수를 구하는 문제
"""

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 탐색을 시작할 좌표값과, 전체 땅 모양을 인자로 받는다.
def bfs(graph, a, b):
    queue = deque()
    queue.append((a,b))
    # 확인한 구역은 0으로 바꾸기
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft() 
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] == 0
                queue.append((nx, ny))
    return

t = int(input()) # 테스트 케이스의 개수

for i in range(t): 
    count = 0
    # 땅을 나타내는 행렬을 0으로 초기화 시켜준다.
    n, m, k = map(int, input().split()) 
    graph = [[0] * m for _ in range(n)] 

    # 배추가 심어져 있는 구간을 입력받고, 해당하는 땅의 좌표를 1로 바꿔준다.
    for j in range(k):                
        x, y = map(int, input().split())                
        graph[x][y] = 1                                                       

    # 땅의 모든 부분에 대하여 배추가 심어져 있는 구간이라면,
    # bfs를 실행하여 인접한 배추가 있는지 확인
    for a in range(n):                              
        for b in range(m):
            if graph[a][b] == 1:
                bfs(graph, a, b)
                count += 1
    print(count)