def solution(N, stages):
    temp = []
    for i in range(N):
        temp.append([])

    bunmo = len(stages)
    bunja = 0
    # 맨 처음 분모는 stages 유저 개수만큼, 그 다음 단계에서는 분모에서 분자를 빼주면 그 다음 단계의 분모가 나온다.
    # 분자는 현재 stage에 해당하는 숫자가 몇 개인지 count하면 된다.
    for i in range(N):
        temp[i].append(i+1)
        bunmo = bunmo-bunja
        bunja = stages.count(i+1)
        # 스테이지에 도전한 사람들의 수가 0이 되어버릴 때 분모가 0이 되므로 런타임 에러가 나기 때문에 따로 예외처리 필요
        if bunmo == 0:
            temp[i].append(0)
        else:
            temp[i].append(bunja/bunmo)
    # print(temp)

    # 일단 실패율이 높은 순으로 정렬하고, 실패율이 같다면 stage의 내림차순으로 정렬한다.
    temp = sorted(temp, key=lambda x: (x[1], -x[0]))
    # print(temp)
    answer = []

    # 현재까지 실패율이 낮은 것부터 높은 순으로 정렬되어있기 때문에 answer에 거꾸로 담아준다.
    for i in range(N):
        answer.append(temp[N-i-1][0])
    # print(answer)

    return answer
