# """
# (n)   사진틀 개수 : 3
# (num) 전체 총 추천 횟수 : 9
# (who) 추천 받은 순서 : 2 1 4 3 5 6 2 7 2
# """
# n = int(input())
# num = int(input())

# # 비교함수
# def is_in_arr(arr, w):
#     for i in arr:
#         if i[2] == w:
#             return True
#     return False

# arr = []
# who = input().split()
# for idx, w in enumerate(who):
#     # 1. 추천받은 학생이 사진틀에 존재하는지 확인한다.
#     if is_in_arr(arr, w):
#         # 2. 존재한다면 해당 사진의 추천수를 증가시키고, 존재하지 않는다면 3번을 수행한다.    
#         for index, value in enumerate(arr):
#             if value[2] == w:
#                 arr[index][0] += 1
#                 break
#     else:
#         # 3. 사진틀이 비어있다면 사진을 추가해주고, 사진틀이 꽉 차있다면 주어진 조건에 따라 사진을 교체한다.
#         if len(arr) < n:
#             arr.append([1, idx, w])            
#         else:
#             arr[0] = [1, idx, w]
            
#     arr.sort(key=lambda x: (x[0], x[1]))

# arr.sort(key=lambda x:int(x[2]))
# # result 
# for i in range(n):
#     if i == n-1:
#         print(arr[i][2])
#     else:
#         print(arr[i][2], end=' ')


# def printSumAvg(x, y, z):
#     sum_data = x + y + z
#     avg = sum_data // 3
#     print("합계 :",sum_data, "평균 :",avg)

# printSumAvg(10, 20, 30)

def return_sum(a, b):
    """인자 a, b 받아 더한 값을 sum_data에 담아 반환합니다."""
    sum_data = a + b
    return sum_data

help(return_sum)