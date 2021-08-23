from itertools import combinations # 순서를 고려하지 않는 조합 

n, s = map(int, input().split())

n_list = list(map(int, input().split()))

count = 0
for i in range(n):
    sub = list(combinations(n_list, i))    
    for j in sub:
        if sum(j) == s:
            count += 1

print(count)


