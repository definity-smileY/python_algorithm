"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

반복 횟수와 문장을 입력받아 여러 번 출력해보자.

예시
n = input()
s = input()
print(int(n)*s)

참고
문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.

입력:
반복 횟수와 문장이 줄을 바꿔 입력된다.
3
I love CS

출력:
입력된 횟수만큼 입력된 문장을 출력한다.
I love CSI love CSI love CS
"""
a = input()
b = input() * int(a)
print(b)
