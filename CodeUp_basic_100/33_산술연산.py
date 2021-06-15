"""
본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

문자 1개를 입력받아 그 다음 문자를 출력해보자.
영문자 'A'의 다음 문자는 'B'이고, 숫자 '0'의 다음 문자는 '1'이다.

예시
...
print(chr(n+1))

참고
숫자는 수를 표현하는 문자로서 '0' 은 문자 그 자체를 의미하고, 0은 값을 의미한다.

힌트
아스키문자표에서 'A'는 10진수 65로 저장되고 'B'는 10진수 66으로 저장된다.
따라서, 문자도 값으로 덧셈을 할 수 있다. 어떤 문자의 값에 1을 더하면 그 다음 문자의 값이 된다.

입력:
문자 1개가 입력된다.


출력:
그 다음 문자를 출력한다.
"""
# 입력받는 문자를 정수로 변환 후 
a = ord(input())
# print(type(a))
# 아스키문자표로 인식 후 다음 값 출력
print(chr(a + 1))
