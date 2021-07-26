import sys
input = sys.stdin.readline
# sys.stdin.readline 말고 그냥 input 쓰면 시간초과
t = int(input())

# 우선 성적 순 정렬, 성적 순 정렬했을 때 1위는 무조건 합격
# 이후 성적 1위의 면접 순위 기준으로 점점 면접 순위가 높은 사람들 합격
for _ in range(t):
    n = int(input())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    a = sorted(a)
    # print(a)
    res = 1
    max_interview = a[0][1]
    for i in range(1, n):
        if a[i][1] < max_interview:
            max_interview = a[i][1]
            res += 1
    print(res)
