n = int(input())

weight = list(map(int, input().split()))
weight = sorted(weight)

# 그리디, 이때까지의 누적합 target이 다음 weight보다 작다면 target 측정 불가
target = 1
for i in weight:
    if target < i:
        break
    target += i

print(target)
