answers = [1, 3, 2, 4, 2]


def solution(answers):
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    answer = []
    result = []

    for i in range(3):
        score = list(
            filter(lambda x: pattern[i][x[0] % len(pattern[i])] == x[1], list(enumerate(answers))))
        answer.append(len(score))

    for idx, score in enumerate(answer):
        if score == max(answer):
            result.append(idx + 1)

    return result


print(solution(answers))
