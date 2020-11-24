from itertools import permutations

numbers = "17"


def solution(numbers):
    # 1. 숫자 case 구하기
    case = []
    for i in range(1, len(numbers) + 1):
        case.extend(permutations(numbers, i))
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
