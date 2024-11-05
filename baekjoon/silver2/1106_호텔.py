from sys import stdin, maxsize

"""
적어도 유치해야 하는 고객 수 C명과 도시의 개수 N이 주어진다. 이때 각 도시에는 홍보비용과 그 비용으로 유치할 수 있는 고객에 대한 정보가 제공된다. 이때, 최소 비용으로 적어도 C명의 고객의 수를 유치하는 경우를 반환하는 문제이다.

결과론적으로 
dp[N명의 고객을 유치하는데 드는 비용] = min(dp[N명의 고객을 유치하는데 드는 비용], dp[N명의 고객을 유치하는데 드는 비용 - 현재 방문한 도시의 유치가능한 인원수] + 입력값 비용)
"""

# C = 명수, n = 도시
human, city = map(int, stdin.readline().split())
# 도시만큼 lst에 [비용, 명수] 추가
lst = []
# 정보
for _ in range(city):
    lst.append(list(map(int, input().split())))

# 적어도 C명을 늘려야 하기에,
dp = [0] + [maxsize] * (human + 100)

# memoization
for cost, cust in lst:
    for cur_cust in range(cust, human + 101):
        dp[cur_cust] = min(dp[cur_cust], dp[cur_cust - cust] + cost)

print(min(dp[human:human + 101]))