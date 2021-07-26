'''
가방을 기준으로 가방에 담을 수 있는 보석 탐색.
최소 힙을 통해 매번 가방에 담을 수 있는 모든 보석을 찾고,
그것들의 가격을 새로운 우선순위 큐(bosuk_can_in_back)에 저장한다.
현재 탐색하는 가방은 이전에 탐색한 가방보다 용량이 더 크거나 같으므로
앞선 가방에 담을 수 있는 보석은 현재 가방에도 담을 수 있어서
다음 가방에 담을 수 있는 보석을 찾을 때는, 이전에 탐색이 끝난 지점에서 이어갈 수 있다.
매번 가방에 담을 수 있는 모든 보석을 찾은 후에는,
그 중 가격이 가장 높은 보석을 최대 힙을 이용하여 가방에 담는다.
'''

import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
bosuk = []
weight = []
for _ in range(n):
    heapq.heappush(bosuk, [int(x) for x in input().split()])
for _ in range(k):
    weight.append(int(input()))

weight = sorted(weight)

res = 0
bosuk_can_in_back = []

for i in weight:

    # bosuk을 우선순위 큐에 저장했으므로 bosuk[0]에는 가장 가벼운 보석의 정보가 들어있음.
    while bosuk and i >= bosuk[0][0]:
        current = heapq.heappop(bosuk)[1]
        # 파이썬에는 최소 힙만 존재하므로, 최대 힙은 - 부호를 통해 구현
        heapq.heappush(bosuk_can_in_back, -current)
    if bosuk_can_in_back:
        # 최대 힙을 통해 가방에 넣을 수 있는 보석의 최대 가격을 res에 더함.
        res -= heapq.heappop(bosuk_can_in_back)
print(res)


# 시간초과코드
# 보석 기준으로 들어갈 수 있는 가방 탐색
# 보석은 비싼 보석부터, 가방은 허용 무게가 작은 것부터
'''
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
bosuk = []
weight = []
for _ in range(n):
    bosuk.append(list(map(int, input().split())))

for _ in range(k):
    weight.append(int(input()))

bosuk = sorted(bosuk, key=lambda x: x[1], reverse=True)
weight = sorted(weight)

full_back_idx = []
res = 0
for i in range(n):
    for j in range(k):
        if weight[j] >= bosuk[i][0] and j not in full_back_idx:
            res += bosuk[i][1]
            full_back_idx.append(j)
            break
    if len(full_back_idx) == k:
        break
print(res)
'''
