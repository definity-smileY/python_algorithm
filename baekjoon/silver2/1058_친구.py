import sys

num = int(input())

# 1. 친구 목록 그래프, 친구가 아닌 사람들에 대한 그래프, 2-친구에 대한 그래프
friend = [[] for i in range(num)] 
no_friend = [[] for i in range(num)]
friend_second =[[] for i in range(num)]

# 2. 입력 데이터를 받아 친구 목록 그래프와 친구가 아닌 사람들에 대한 그래프 분배
for i in range(num):
    for idx, v in enumerate(input()): # 돌때마다 해당 인덱스에 idx 추가하기
        if v == 'Y':
            friend[i].append(idx)        
        elif v == 'N' and i != idx: 
            no_friend[i].append(idx)

# 3. 친구가 아닌 사람들에 대한 그래프 중 2-친구 관계에 있는지 확인
for idx, v in enumerate(no_friend):
    for name in v:
        # 4. 2-친구 조건에 합당하면 2-친구에 대한 그래프에 추가
        if len(set(friend[name]) - set(friend[idx])) != len(friend[name]):
            friend_second[idx].append(name)

m = 0
for i in range(num):
    if m < len(friend[i] + friend_second[i]):
        m = len(friend[i] + friend_second[i])
print(m)