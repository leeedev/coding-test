from itertools import permutations

numbers = "12"


def solution(numbers):
    # 1. 숫자 case 구하기
    case = []

    # i가 1부터 2까지 돌아감
    for i in range(1, len(numbers) + 1):
      # i가 1일때 [('1',), ('7',)]
      # i가 2일때 [('1', '7'), ('7', '1')]
        case.extend(permutations(numbers, i))

    # case = [('1',), ('7',), ('1', '7'), ('7', '1')]에서
    # case = {1, 7, 17, 71}로 int type으로 합치고 중복 제거
    case = set(int("".join(i)) for i in case)

    # 2. 소수인지 확인
    answer = 0
    for number in case:
        if number != 0 and number != 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                answer += 1

    return answer


print(solution(numbers))
