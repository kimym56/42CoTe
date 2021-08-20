from collections import deque


def solution(priorities, location):
    answer = 0
    que = deque(priorities)
    idx = deque(list(range(len(priorities))))

    while que:
        if que[0] == max(que):
            answer += 1
            que.popleft()
            if idx.popleft() == location:
                break
        else:
            que.append(que.popleft())
            idx.append(idx.popleft())

    return answer
