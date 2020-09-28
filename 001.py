"""
반복문을 사용하여 0부터 n까지의 합 출력하기
"""

def print_to_n(n):
    i = 0
    sum = 0
    while (i <= n):
        sum = sum + i
        i = i + 1
    print(sum)

if __name__ == "__main__":
    print_to_n(100)

# def print_sum(n):

#     for i in range(print_sum(n)):
#         print(i)
# if __name__ == "__mian__":
#     print_sum(100)