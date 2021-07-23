def solution(answers):
    # 찍는 답안의 배열
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 몇 번 찍어서 맞췄는 지 count
    c1, c2, c3 = 0, 0, 0

    for i in range(len(answers)):
        # 사람마다 찍는 답안의 규칙성과 돌아오는 주기에 따라 인덱스 조절
        i1 = i % 5
        i2 = i % 8
        i3 = i % 10

        if a1[i1] == answers[i]:
            c1 += 1
        if a2[i2] == answers[i]:
            c2 += 1
        if a3[i3] == answers[i]:
            c3 += 1

    temp = max(c1, c2, c3)
    answer = []
    if temp == c1:
        answer.append(1)
    if temp == c2:
        answer.append(2)
    if temp == c3:
        answer.append(3)
    return answer
