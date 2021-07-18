import math

def get_pow(N):
    return int(math.pow(N, 2))

if __name__ == '__main__':
    a, b, c, d, e = map(int, input().split())
    print(((get_pow(a)+get_pow(b)+get_pow(c)+get_pow(d)+get_pow(e)) % 10))