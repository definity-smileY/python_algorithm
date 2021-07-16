# """
# INPUT
# 3
# 2 3 1

# 4
# 2 4 1 3
# OUTPUT

# """
# data = int(input()) 
# stick1 = list(map(int, input().split())) # 1번 장대
# stick2 = [] # 2번 장대
# result = [] # 결과값 

# data = data # 3번 장대로 옮겨야할 값
# flag = True # True : stick1 / False : stick2

# while data > 0 : # input값이 0보다 클 경우
#     if flag: # True
#         while stick1:
#             if stick1[-1] == data: # 1번 장대 맨 위에 값이 인풋값과 같다면
#                 result.append((1, 3)) # 1번 -> 3으로 명시
#                 stick1.pop() 
#                 data -= 1 # after = 2
#             else: 
#                 result.append((1, 2)) # 1번 -> 2으로 명시
#                 stick2.append(stick1.pop()) # stick1에 값을 stick2에 옮기기
#         flag = False
#     else:
#         while stick2:
#             if stick2[-1] == data: # 2번 장대 맨 위에 값이 인풋값과 같다면
#                 result.append((2, 3)) # 2번 -> 3으로 명시
#                 stick2.pop()
#                 data -= 1
#             else:
#                 result.append((2, 1)) # 2번 -> 1으로 명시
#                 stick1.append(stick2.pop())
#         flag = True

# print(len(result))
# for a, b in result:
#     print(a, b)

import sys

a, b = map(int, sys.stdin.readline().split())

def main(a, b):
    for i in range(a+1):
        print(i)

main(a, b)


# def solution(v):
#     answer = []
#     v1 = []
#     v2 = []
#     for i in v:
#         if i[0] not in v1:
#             v1.append(i[0])
#         else:
#             v1.remove(i[0])

#         if i[1] not in v2:
#             v2.append(i[1])
#         else:
#             v2.remove(i[1])

#     answer = v1 + v2 
#     # print(answer)
#     return answer

# solution([[1, 4], [3, 4], [3, 10]])

# def solution(v):
#     answer = []
#     answer.append(v[0][0]^v[1][0]^v[2][0])
#     answer.append(v[0][1]^v[1][1]^v[2][1])
#     print(answer)
#     return answer
# solution([[1, 4], [3, 4], [3, 10]])