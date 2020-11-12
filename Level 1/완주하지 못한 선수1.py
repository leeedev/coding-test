from collections import Counter

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]


print(solution(participant, completion))
