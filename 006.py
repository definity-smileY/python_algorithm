"""
숫자 뒤집기
"""

print(123 % 10) # 1의 자리수 == 3
print(int(123 / 10) % 10) # 10의 자리수 == 2
print(int(123 / 100) % 100)  # 100의 자리수 == 1



def solve(n):
    if n == 0:
        return 0

    print(n%10, end=' ') #자릿수 출력
    solve(n//10)


    # f(n//10) # 1의 자리, 10의 자리, 100의 자리의 순서로 재귀 함수를 호출한다.

if __name__ == "__main__":
    num_str = input("입력 :")
    num = int(num_str)
    solve(num)
