from collections import deque
def solution(priorities, location):
    que=deque()
    for i in range(len(priorities)):
        que.append((i,priorities[i]))
    count = 1
    while que:
        if que[0][1]==max(que,key=lambda x:x[1])[1]:
            if que[0][0]==location:
                return count;
            else:
                que.popleft()
                count+=1    
        else:
            que.append(que.popleft())
    return count
