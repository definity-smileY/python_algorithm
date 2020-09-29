"""
3과 5의 배수 계산하기
"""

def check_common(n):
    i = 1
    while n >= i:
        if (i % 3 == 0 ) and (i % 5 == 0):
            print('%d' %i)
        i += 1

if __name__=='__main__':
    check_common(100)