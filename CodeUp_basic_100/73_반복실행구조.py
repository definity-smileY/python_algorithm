"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

while 조건식 :
  ...
  ...

반복 실행구조를 사용해 보자.

참고
조건검사, 출력, 감소의 순서와 타이밍을 잘 생각해보자.

입력:
정수 1개가 입력된다.
(1 ~ 100)
5

출력:
1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력한다.

4
3
2
1
0
"""
a = int(input())
while a > 0:
    a = a - 1
    print(a)