brown = 10
yellow = 2


def solution(brown, yellow):
    multiply = brown + yellow
    divisor = []

    # multiply의 약수 w, h(yellow가 1 이상이므로 brown은 3 이상)
    for i in range(3, int(multiply ** 0.5 + 1)):
        if multiply % i == 0:
            divisor.append(i)

    if len(divisor) == 1:
        return [int(multiply / divisor[0]), divisor[0]]

    # w + h = brown / 2 + 2를 만족하는 w, h
    for i in range(0, len(divisor)):
        h = divisor[i]
        w = int(multiply / h)
        if w + h == brown / 2 + 2:
            return [w, h]


print(solution(brown, yellow))
