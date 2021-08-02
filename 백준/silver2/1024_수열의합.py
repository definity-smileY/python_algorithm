"""
수열의 합의 식 = n째 항까지의 합을 구하는 공식

합 = (x + 1) + (x + 2) + (x + 3) + ... (x + l)
"""
n, l = map(int, input().split()) # 합, 길이

for i in range(l, 101): # 길이
    # 공식
    x = n - (i * (i + 1) / 2) 

    if x % i == 0: # 나누어 떨어진다면
        x = int(x // i)

        if x >= -1:
            for j in range(1, i + 1):
                print(x + j, end=' ')            
            break

# 길이가 100보다 크거나 그러한 수열이 없을 때 -1 출력
else:
    print(-1)
