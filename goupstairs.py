N1 = 1
N2 = 3
N3 = 5


def solution(stairs, energy2, energy3):
    if stairs <= 0:
        return 0
    if energy2 == 4 or energy3 == 2:
        stairs -= 3
        energy2 = 0
        energy3 = 0
    E1 = solution(stairs - 1, 0, 0) + N1
    E2 = solution(stairs - 2, energy2 + 1, 0) + N2
    E3 = solution(stairs - 3, 0, energy3 + 1) + N3
    if stairs < 3:
        E3 = 0
    if stairs < 2:
        E2 = 0
    if stairs == 1:
        return N1
    return max(E1, E2, E3)


if __name__ == "__main__":
    print solution(10, 0, 0)
