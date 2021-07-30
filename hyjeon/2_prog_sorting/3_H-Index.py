def solution(citations):
    citations.sort()
    citlen = len(citations)

    for i in range(citlen):
        # citations[i]: 해당 논문 인용한 횟수, citlen-i: i번 이상 인용한 논문의 횟수
        if citations[i] >= citlen-i:
            return citlen-i
    # [0,0,0]->0 일 때는 위의 for문만 있으면 0이 아닌 null을 리턴해서 밑에 return 0 필요
    return 0
