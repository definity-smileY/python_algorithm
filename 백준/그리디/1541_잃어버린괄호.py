"""
양수, +, -, () 
목적 : 괄호를 적절히 쳐서 이 식의 값을 최소로 만들자.
포인트 : 최초로 마이너스가 나오기 전까지 나오는 숫자는 모두 더할 수 밖에 없으며, 이후 마이너스가 나오는 순간 그 뒤에 있는 모든 숫자들을 빼주면 된다.
"""

a = input().split('-') # (1) 입력값을 먼저 - 기준으로 나누고

sum = 0

for i in a[0].split("+"): # (2) - 기준 앞에 인덱스들은 다 더하고
    print(i)
    sum += int(i)

for i in a[1:]: # (3) 그 뒤로 sum 값들 나온 값들로 부터 빼준다.
    for j in i.split('+'): 
        sum -= int(j)

# print(sum)

# 60–55+45–25+20 : (1) [60, 55+45, 25+20] (2) sum = 60 (3) 55+45, 25+20 => 55, 45, 25, 20
# 55-50+40
# 44+50-45+25-20