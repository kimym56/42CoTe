# x*y=brown+red, (x-2)*(y-2)=red 연립해서 풀어서 x=~, y=~ 식으로 나타낸다.
def solution1(brown, yellow):
    x = (brown+4+((brown+4)**2-16*(brown+yellow))**0.5)/4
    y = (brown+yellow)//x
    return [max(x, y), min(x, y)]


# brute force 이용
def solution2(brown, yellow):
    # 가로 또는 세로로 길 수 있는 최대 길이
    max_len = brown // 2

    # 세로부터 for문 -> 세로<=가로
    for h in range(3, max_len):
        for w in range(3, max_len):
            if (w+h)*2-4 == brown and (w-2)*(h-2) == yellow:
                return [w, h]
