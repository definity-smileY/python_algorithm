import sys
import heapq

n = int(input()) # 강의의 개수

heapqueue = [] # 시작시간, 끝나는시간, 번호 / 시작시간 기준으로 정렬해놓은 힙큐
q = [] # 종료시간

for _ in range(n):
    num, start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(heapqueue, [start, end, num])

start, end, num = heapq.heappop(heapqueue) # heapqueue.pop()
heapq.heappush(q, end)

while heapqueue:
    start, end, num = heapq.heappop(heapqueue)

    if q[0] <= start: # 종료시간 <= 시작시간
        heapq.heappop(q)
    heapq.heappush(q, end)

print(len(q))