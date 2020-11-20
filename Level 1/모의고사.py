answers = [1, 3, 2, 4, 2]


def solution(answers):
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = []
    result = []

    for i in range(3):
        score = list(
            filter(lambda x: pattern[i][x[0] % len(pattern[i])] == x[1], list(enumerate(answers))))
        scores.append(len(score))

    for idx, score in enumerate(scores):
        if score == max(scores):
            result.append(idx + 1)

    return result


print(solution(answers))
