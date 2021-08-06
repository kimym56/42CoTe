import sys
import heapq

input = sys.stdin.readline
n = int(input())

left = []
right = []

# left는 최대힙, right는 최소힙
# 중앙값 기준으로 작거나 같은 값 = left, 큰 값 = right
# 외친 수가 짝수개일 때 중간에 있는 두 수 중 작은 수를 말해야하기 때문에 중간값은 left에 있어야 함

for i in range(n):
    num = int(input())
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    # left에서 가장 작은 원소가 right에서 가장 작은 원소보다 클 때 swap
    # left에 있는 원소가 항상 right에 있는 모든 원소보다 작아야 함
    if right and left[0][1] > right[0][1]:
        left_val = heapq.heappop(left)[1]
        right_val = heapq.heappop(right)[1]
        heapq.heappush(right, (left_val, left_val))
        heapq.heappush(left, (-right_val, right_val))
    print(left[0][1])
