"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

실수 2개(f1, f2)를 입력받아 곱을 출력하는 프로그램을 작성해보자.

예시
...
m = float(f1) * float(f2)
print(m)

참고
수 * 수는 곱(multiplication)이 계산된다.

입력:
2개의 실수가 공백으로 구분되어 입력된다.

출력:
첫 번째 실수와 두 번째 실수를 곱한 값을 출력한다.
"""

a, b = input().split()
c = float(a) * float(b)
print(c)