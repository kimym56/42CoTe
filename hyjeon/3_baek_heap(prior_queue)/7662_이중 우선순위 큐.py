import sys
import heapq
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    visit = [False] * 999999

    order_num = int(input())

    for key in range(order_num):
        order = input().split()
        if order[0] == 'I':
            heapq.heappush(min_heap, (int(order[1]), key))
            heapq.heappush(max_heap, (int(order[1]) * -1, key))
            visit[key] = True  # True이면 어떤 힙에서도 아직 삭제되지 않은 상태

        elif order[0] == 'D':
            # 삭제연산 시, key값을 기준으로 해당 노드가 다른 힙에서 삭제된 노드인가를 먼저 판단한다.
            if order[1] == '-1':
                # 이미 상대힙에 의해 삭제된 노드인 경우 삭제되지 않은 노드가 나올 때까지 계속 버리다가 이후 삭제대상노드가 나오면 삭제한다.
                # visit이 False일 때 -> 해당노드가 삭제된 상태
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)  # 버림 (상대힙에서 이미 삭제된 노드이므로)
                if min_heap:
                    # visit이 True였으므로 False로 바꾸고 내가 삭제함
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif order[1] == '1':
                # 이미 삭제된 노드인 경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

# 모든 연산이 끝난 후에도 쓰레기 노드가 들어있을 수 있으므로, 결과를 내기 전 모두 비우고 각 힙의 첫번째 원소값을 출력한다.
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')


# 시간초과 풀이(maxheap, minheap을 그때마다 -1 곱해가면서 heap 하나 사용)
input = sys.stdin.readline


def allminus(heap):
    new = []
    for i in range(len(heap)):
        heapq.heappush(new, -1*heap[i])
    return new


t = int(input())
for i in range(t):
    heap = []
    n = int(input())
    for j in range(n):
        op, num = input().split()
        num = int(num)
        print(num)
        if (op == 'I'):
            heapq.heappush(heap, num)
        else:
            if (num == 1):
                if heap:
                    heap = allminus(heap)
                    heapq.heappop(heap)
                    heap = allminus(heap)

            else:
                if heap:
                    heapq.heappop(heap)
        # print(heap)
    print(heap)
    if heap:
        heap = allminus(heap)
        print(heap[0]*(-1), end=' ')
        heap = allminus(heap)
        print(heap[0])
    else:
        print("EMPTY")
