from itertools import permutations

numbers = [2, 1, 3, 4, 1]


def solution(numbers):
    answer = []
    l = list(permutations(numbers, 2))
    for i in l:
        answer.append(i[0] + i[1])
    return sorted(list(set(answer)))


print(solution(numbers))
