"""
재귀 호출을 사용하여 n부터 1까지 출력하기
"""

def print_to_n(n):
    answer = 1
    
    if n >= answer:
        print(n)
        print_to_n(n-1)

if __name__=='__main__':
    print_to_n(10)