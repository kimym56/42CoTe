import math
from itertools import permutations


def is_prime(n):
    # 0, 1은 소수가 아님
    if n < 2:
        return 0

    # 2부터 sqrt(n)까지만 나눠보고 나누어 떨어지는 지 확인하면 소수 판별 완료
    else:
        for i in range(2, int(math.sqrt(n))+1):  # 원래 math.sqrt(n)하면 float
            if n % i == 0:
                return 0
    return 1


def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        # permutations 순열을 사용하여 모든 경우의 수 따져보기
        arr = list(permutations(numbers, i))

        # arr은 [('1', '7'), ('7', '1')] 이런 형태(각각 17, 71이 되어야 함)이기 때문에 join 해준다
        for j in range(len(arr)):
            num = int(''.join(map(str, arr[j])))
            if is_prime(num):
                answer.append(num)

    # 중복 제거하기 위해 set 사용
    answer = list(set(answer))
    return len(answer)
