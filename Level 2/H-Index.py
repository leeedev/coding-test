citations = [3, 0, 6, 1, 5]


def solution(citations):
    n = len(citations)
    for i in range(n, -1, -1):
        if i <= len(list(filter(lambda x: x >= i, citations))):
            return i


print(solution(citations))
