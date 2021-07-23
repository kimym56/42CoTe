# 합이 2인경우는 padding+열쇠의 홈이라고 생각해서 2일때는 모두 가능하다고 생각했으나 열쇠의 돌기, 자물쇠의 돌기가 만나면 1+1=2가 되어서 이 부분 예외처리 필요->padding=5로 변경
# 처음에 열쇠 한칸씩 이동시킬때 열쇠의 범위에서만 확인해버림->lock 기준으로 확인했어야함
# key rotation 부분을 안일하게 3*3 예시로만 돌려서 rotation 로직 틀림

def rotation(key):
    n = len(key)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = key[i][j]
    return ret

# entire에 key를 넣어보고 entire 성공했는 지 확인한 후 key를 다시 빼준다.


def check_sup(x, y, key, entire):
    answer = True
    for i in range(0, len(key)):
        for j in range(0, len(key)):
            entire[x+i][y+j] += key[i][j]

    for i in range(0, len(entire)):
        for j in range(0, len(entire)):
            if entire[i][j] != 1 and entire[i][j] != 5 and entire[i][j] != 6:
                answer = False
                break

    for i in range(0, len(key)):
        for j in range(0, len(key)):
            entire[x+i][y+j] -= key[i][j]

    return answer

# entire 배열 내에서 각각의 key 크기만큼 움직이면서 탐색하기 위해 x, y 좌표값 조절


def check(key, entire, listlen):
    x, y = 0, 0
    while (1):
        answer = True
        answer = check_sup(x, y, key, entire)

        if answer == True:
            return True

        y += 1

        if (y == listlen+1-len(key)):
            y = 0
            x += 1

        if (x == listlen+1-len(key)):
            x = 0
            y = 0
            break

    return answer


def solution(key, lock):
    answer = False
    listlen = len(key)*2 + len(lock)-2
    entire = [[5 for _ in range(listlen)]
              for _ in range(listlen)]  # padding값 5로 조절

    for i in range(0, len(lock)):
        for j in range(0, len(lock)):
            entire[i+len(key)-1][j+len(key)-1] = lock[i][j]

    answer = check(key, entire, listlen)

    if answer == True:
        return answer
    for i in range(3):
        key = rotation(key)
        answer = check(key, entire, listlen)
        if answer == True:
            break

    return answer
