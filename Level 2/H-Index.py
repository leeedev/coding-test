citations = [3, 0, 6, 1, 5]


def solution(citations):
    n = len(citations)
    for h in range(n, -1, -1):
        if h <= len(list(filter(lambda x: x >= h, citations))):
            return h


print(solution(citations))
