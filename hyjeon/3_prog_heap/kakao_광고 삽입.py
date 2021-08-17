def convert(time):
    h, m, s = time.split(":")
    return int(h)*3600 + int(m)*60 + int(s)


def solution(play_time, adv_time, logs):
    playSec = convert(play_time)
    advSec = convert(adv_time)
    total = [0 for _ in range(playSec+1)]

    for log in logs:
        start, end = log.split("-")
        startSec = convert(start)
        endSec = convert(end)
        total[startSec] += 1
        total[endSec] -= 1

    for i in range(1, len(total)):
        total[i] += total[i-1]

    currentSum = sum(total[:advSec])
    maxSum = currentSum
    maxId = 0

    for i in range(advSec, playSec):
        currentSum = currentSum+total[i]-total[i-advSec]
        if currentSum > maxSum:
            maxSum = currentSum
            maxId = i-advSec+1

    answer = '%02d:%02d:%02d' % (maxId/3600, maxId/60 % 60, maxId % 60)

    return answer
