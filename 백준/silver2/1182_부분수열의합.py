from itertools import combinations # 순서를 고려하지 않는 조합 

n, s = map(int, input().split())

n_list = list(map(int, input().split()))

count = 0
for i in range(n):
    sub = list(combinations(n_list, i))
    print("sub == ", sub)
    for j in sub:
        # print(j)
        print("j == ", j)
        if sum(j) == s:
            print("sum(j) == 0", sum(j))
            count += 1

print(count)


