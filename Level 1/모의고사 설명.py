answers = [1, 3, 2, 4, 2]


def solution(answers):
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = []
    result = []

    # list(enumerate(answers)) = [(0, 1), (1, 3), (2, 2), (3, 4), (4, 2)]
    # (x의 첫번째 요소 % pattern의 길이)에 있는 pattern = x의 두번째 요소
    for i in range(3):
        score = list(
            filter(lambda x: pattern[i][x[0] % len(pattern[i])] == x[1], list(enumerate(answers))))
        scores.append(len(score))

#  scores = [2, 2, 2]
    for idx, score in enumerate(scores):
        if score == max(scores):
            result.append(idx + 1)

    return result


print(solution(answers))


# enumerate을 하면 tuple형태로 (idx,값)인 배열을 리턴함.
# pattern과 answers와 일치(정답)하는 answers의 길이 == score
# score의 길이를 scores 배열에 넣음
# 최대값이 여러개일 수 있으므로 scores를 enumerate함. => (idx, score)
# 최대 score값을 가지는 idx를 result배열에 넣어서 리턴함
