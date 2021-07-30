def solution(numbers):
    answer = list(map(str, numbers))

    # lambda x:x*3 은 해당 문자열을 3개 나열하여 비교
    # ['9','5','34','3','30'] -> 303030->333->343434->555->999
    answer.sort(key=lambda x: x*3, reverse=True)
    # print(int(''.join(answer)))

    # int해주는 이유는 [0,0,0] 들어왔을 때 000이 아닌 0을 리턴해주기 위함
    # str로 바꾸는 건 int가 너무 클 때 방지하기 위함 -> 위에 int 값 큰 걸로 print할 때는 잘 나오지만 return 할 때 int만 있으면 큰 수가 이상하게 나온다.
    return str(int(''.join(answer)))
