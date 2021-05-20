# 값으로 이뤄진 불변(immutable) 순서쌍을 만들어낼 수 있는 tuple 내장 타입
# 가장 짧은 튜플은 딕셔너리의 키-값 쌍과 비슷하게 두 값으로 이루어짐
snack_calories = {
    '감자칩': 140,
    '팝콘' : 80,
    '땅콩' : 190,
}
items = tuple(snack_calories.items())
print(items)

"""
>>> (('감자칩', 140), ('팝콘', 80), ('땅콩', 190))
"""


# 튜플에 있는 값을 숫자 인덱스로 접근
item = ('호박엿', '식혜')
first = item[0]
second = item[1]
print(first, '&', second)

"""
>>> 호박엿 & 식혜
"""

# 튜플이 만들어지면, 인덱스를 통해 새 값을 대입해서 튜플을 변경할 수 없다.
pair = ('약과', '호박엿')
pair[0] = '타래과'

"""
>>> Traceback (most recent call last):
    TypeError: 'tuple' object does not support item assignment
"""


# 언패킹(unpacking) 구문
# 언패킹 구문을 사용하면 한문장 안에서 여러 값을 대입 o
# 언패킹 문에 사용한 패턴은 튜플을 변경하려고 시도할 때 사용한 구문,
# 즉 파이썬이 허용하지 않았던 구문과 아주 비슷하지만, 두 구문은 매우 다르게 작동

# ex) 튜플이 쌍이라는 사실을 알고있다면, 인덱스를 사용해 각 값에 접근하는 대신 이 튜플을 두 변수 이름으로 이뤄진 튜플에 대입가능
item = ('호박엿', '식혜')
first, second = item #언패킹
print(first, '&', second)

"""
>>> 호박엿 & 식혜
"""


# 언패킹은 튜플 인덱스를 사용하는 것보다 시각적인 잡음이 적다.
# 리스트, 시퀀스, 이터러블(iterable)안에 여러 계층으로 이터러블이 들어간 경우 등 다양한 패턴을 언패킹 구문에 사용가능

# 다음 코드를 작성하는 것을 추천하진 않지만, 이런 코드도 가능하며 어떻게 작동하는지 이해하는 것은 중요하다.
favorite_snack = {
    '짭조름한 과자': ('프레즐', 100),
    '달콤한 과자': ('쿠키', 180),
    '채소': ('당근', 20),
}

((type1, (name1, cals1)),
(type2, (name2, cals2)),
(type3, (name3, cals3))) = favorite_snack.items()

print(f'제일 좋아하는 {type1} 는 {name1}, {cals1} 칼로리입니다.')
print(f'제일 좋아하는 {type2} 는 {name2}, {cals2} 칼로리입니다.')
print(f'제일 좋아하는 {type3} 는 {name3}, {cals3} 칼로리입니다.')

"""
>>> 제일 좋아하는 짭조름한 과자 는 프레즐, 100 칼로리입니다.
    제일 좋아하는 달콤한 과자 는 쿠키, 180 칼로리입니다.
    제일 좋아하는 채소 는 당근, 20 칼로리입니다.
"""