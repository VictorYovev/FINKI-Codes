from constraint import *


def is_attack(q1, q2):
    # check vertical/horizontal
    # check diagonals
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return False
    elif abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return False
    return True


if __name__ == '__main__':
    n = int(input())
    problem = Problem()
    vars = range(1, n + 1)
    domains = [(i, j) for i in range(0, n) for j in range(0, n)]
    problem.addVariables(vars[:], domains)

    for queen1 in vars:
        for queen2 in vars:
            if queen1 < queen2:
                problem.addConstraint(is_attack, (queen1, queen2))

    if n <= 6:
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())
