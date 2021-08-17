N = int(input())
top = list(map(int, input().split()))
stack = []
ans = []

for i in range(N):
    while stack:
        if stack[-1][1] > top[i]:  # [-1][1] 이므로 stack 맨 끝쪽에서 1번째 배열에서 1번째 데이터를 top[i]와 비교
            # 배열은 0번째부터, 수신탑은 1번부터 시작하므로 수를 맞춰주고 ans에 데이터 추가하기
            ans.append(stack[-1][0] + 1)
            break
        stack.pop()  # 배열의 맨 끝 데이터 비우기

    if not stack:
        ans.append(0)  # 스택이 비면 레이저를 수신한 탑이 없다는 뜻이므로 ans에 "0" 데이터 추가

    stack.append([i, top[i]])  # 스택에 현재 신호탑 데이터 추가

for i in range(N):
    print(ans[i], end=' ')
