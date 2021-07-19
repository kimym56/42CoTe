import math
count = 0
prime = []
def is_prime(x):
    if int(x) == 1 or int(x) == 0:
        return False
    for i in range(2, int(math.sqrt(int(x)))+1):
        if int(x) % i == 0:
            return False
    return True
def make_num(number,lst):
    global count
    if number!="" and is_prime(number) and (int(number) in prime)==False:
        prime.append(int(number))
        count = count +1
    for i in lst:
        lst2 = lst[:]
        lst2.remove(i)
        make_num(number+i,lst2)

def solution(numbers):
    global count
    num = [char for char in numbers]
    make_num("",num)
    answer = count
    print(prime)
    return answer
