from collections import deque

N, K = map(int, input().split())
name_len = [len(input()) for _ in range(N)]  # 이름의 길이만 리스트에 담는다.
cnt = 0					# 좋은 친구 수
list = [deque() for _ in range(21)]  # 이름 길이 별로 등수 저장할 리스트. 안에는 큐 구조.

# i: 등수 - 1, v: 이름 길이
for i, v in enumerate(name_len):
    # 큐가 비어있지 않고, 큐[0]과 현재 학생의 등수가 K 이상 차이나면 popleft()
    while list[v] and i - list[v][0] > K:
        list[v].popleft()
        # 큐 안에 있는 등수의 학생들은 현재 학생과 좋은 친구
        # 큐 안의 원소 수 만큼 cnt 증가
    if list[v]:
        cnt += len(list[v])
        # 큐에 현재 학생 append
    list[v].append(i)

print(cnt)
