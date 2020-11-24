n = 6
times = [7, 10]


def solution(n, times):
    # 1명 이상이므로 0으로 하지 않았음
    # 최소시간 ~ 최대시간 * n명
    start = min(times)  # 7분
    end = max(times) * n  # 60분

    # 이분 탐색
    while start <= end:
        # 시작시간과 종료시간의 절반: mid = 33분
        mid = (start + end) // 2
        # 33분동안 7명이 완료함. count = 7명
        count = sum(mid//time for time in times)
        if count == n:
            # 종료시간은 time의 배수여야 함
            overtime = min(mid % time for time in times)
            return mid - overtime
        elif n < count:
            end = mid-1
        elif count < n:
            start = mid+1
    # n = 1이고 times = [2, 2]일때
    # start = 2, end = 2
    # mid = 2, count = 2 첫 회전에 이미 답이 나왔는데 계속 돌리면
    # n < count니까 end = 1이 되어버림
    # start를 반환함
    return start


print(solution(n, times))
