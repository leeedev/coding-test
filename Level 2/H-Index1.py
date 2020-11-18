citations = [3, 0, 6, 1, 5]


def solution(citations):
    s, e = 0, 1000
    while s <= e:
        m = (s + e) // 2
        cnt = 0
        for c in citations:
            if c >= m:
                cnt += 1
        if cnt >= m:
            s = m + 1
        else:
            e = m - 1
    return e


print(solution(citations))
