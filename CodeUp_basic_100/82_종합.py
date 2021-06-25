"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

친구들과 함께 3 6 9 게임을 하던 영일이는 잦은 실수 때문에 계속해서 벌칙을 받게 되었다.
3 6 9 게임의 왕이 되기 위한 369 마스터 프로그램을 작성해 보자.

** 3 6 9 게임은?
여러 사람이 순서를 정한 후, 순서대로 수를 부르는 게임이다.
만약 3, 6, 9 가 들어간 수를 자신이 불러야 하는 상황이라면, 수를 부르는 대신 "박수(X)" 를 쳐야 한다.
33과 같이 3,6,9가 두 번 들어간 수 일때, "짝짝"과 같이 박수를 두 번 치는 형태도 있다. 

참고 
...
for i in range(1, n+1) :
  if i%10==3 :
    print("X", end=' ')    #출력 후 공백문자(빈칸, ' ')로 끝냄
...

입력:
30 보다 작은 정수 1개가 입력된다.
(1 ~ 29)
9


출력:
1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다.
1 2 X 4 5 X 7 8 X
"""
a = int(input())
for i in range(1, a+1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        i = "X"
    print(i, end=' ')