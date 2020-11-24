n = 6
times = [7, 10]


def solution(n, times):
    start = min(times)
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2
        count = sum(mid//time for time in times)
        if count == n:
            overtime = min(mid % time for time in times)
            return mid - overtime
        elif n < count:
            end = mid-1
        elif count < n:
            start = mid+1
    return start


print(solution(n, times))
