def solution(array, commands):
    answer = []
    for t in range(len(commands)):
        i = commands[t][0]
        j = commands[t][1]
        k = commands[t][2]
        new = []
        # i번째부터 j번째까지 new 배열에 담고 sort
        for _ in range(j-i+1):
            new.append(array[i-1])
            i = i+1
        new = sorted(new)
        answer.append(new[k-1])
    return answer
