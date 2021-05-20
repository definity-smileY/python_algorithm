from urllib.parse import parse_qs
# 문자열 인자로 제공된 쿼리 문자열을 구문 분석, 데이터는 이름, 값 쌍의 리스트로 반환되는 모듈

my_values = parse_qs("빨강=5&파랑=0&초록=", keep_blank_values=True)
# keep_blank_values : 선택적 인자, 퍼센트 인코딩된 쿼리의 빈 값을 빈 문자열로 처리해야 하는지를 나타내는 플래그
# 참값은 빈 값을 빈 문자열로 유지해야 함을 나타냄, 기본 거짓 값은 빈 값이 무시되고 포함되지 않는 것처럼 처리됨  

print(repr(my_values))
# repr : __repr__ 공식적인(official) 문자열

"""
>>> {'빨강': ['5'], '파랑': ['0'], '초록': ['']}
"""

# 딕셔너리에 get 메서드를 사용하면 상황에 따라 다른 값이 반환

print('빨강:', my_values.get('빨강'))
print('초록:', my_values.get('초록'))
print('투명도:', my_values.get('투명도'))

"""
>>> 빨강: ['5']
    초록: ['']
    투명도: None
"""
# 파라미터가 없거나 비어 있을 경우 0이 디폴트 값으로 대입되면 좋을 것이다.

# 질의 문자열이 '빨강=5&파랑=0&초록=' 인 경우
red = my_values.get('빨강', [''])[0] or 0
green = my_values.get('초록', [''])[0] or 0
opacity = my_values.get('투명도', [''])[0] or 0

print(f'빨강: {red!r}')
print(f'초록: {green!r}')
print(f'투명도: {opacity!r}')
# !r : 간격을 두고 인쇄하라는 옵션 ex: {!r:15s} : key 문자열의 시작위치부터 15string 만큼 간격을 두고,
# 이어서 다음의 문자열(':{values}')을 인쇄

"""
>>> 빨강: '5'
    초록: 0
    투명도: 0
"""

red = int(my_values.get('빨강', [''])[0] or 0)
# 현재 이 코드는 너무 읽기 어렵고, 시각적 잡음이 많다. 즉 , 코드를 이해하기 쉽지 않으므로, 코드를 새로 읽는 사람이
# 이 식이 실제로 어떤 일을 하는지 이해하기 위해 너무 많은 시간을 투자해야 한다.

# if/else 조건식(또는 삼항 조건식)이 있다.
red_str = my_values.get('빨강', [''])
red = int(red_str[0]) if red_str[0] else 0

# 모든 로직을 분리한 다음 코드를 살펴보자
green_str = my_values.get('초록', [''])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0

# 반복 적용하려면 (단지 두세 번에 불과할지라도) 꼭 도우미 함수를 작성해야 한다.
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        return int(found[0])
    return default

green = get_first_int(my_values, '초록')
print('이것은! :',green)