n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0

# a는 내림차순, b는 오름차순으로 해서 하나씩 각각 곱하면 최솟값
for i in range(n):
    res += a.pop(a.index(min(a)))*b.pop(b.index(max(b)))
print(res)
