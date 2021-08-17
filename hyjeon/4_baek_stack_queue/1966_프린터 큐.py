from collections import deque
import sys
input = sys.stdin.readline

testnum = int(input())
que = deque()

for i in range(testnum):
    docunum, target = list(map(int, input().split()))
    que = deque(list(map(int, input().split())))
    idx = deque(list(range(docunum)))
    cnt = 0
    while que:
        if que[0] == max(que):
            cnt += 1
            que.popleft()
            if idx.popleft() == target:
                print(cnt)
                break
        else:
            que.append(que.popleft())
            idx.append(idx.popleft())
