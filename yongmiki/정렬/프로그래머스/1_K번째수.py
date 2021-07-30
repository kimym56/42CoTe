def solution(array, commands):
    answer = []
    for c in commands:
        new_arr = array[c[0]-1:c[1]]
        new_arr.sort()
        answer.append(new_arr[c[2]-1])
    return answer
arr = [1, 5, 2, 6, 3, 7, 4]
com =	[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr,com))
