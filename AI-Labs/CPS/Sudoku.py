from constraint import *

if __name__ == '__main__':
    cin = input()
    problem = Problem(eval(cin)())
    fields = range(0, 81)
    domains = range(1, 10)
    problem.addVariables(fields, domains)

    # check horizontal
    for row in range(0, 73, 9):
        problem.addConstraint(AllDifferentConstraint(), range(row, (row + 8) + 1))
    # check vertical
    for col in range(0, 9):
        problem.addConstraint(AllDifferentConstraint(), range(col, (col + 72) + 1, 9))

    # check block
    for block in range(0, 7, 3):
        problem.addConstraint(AllDifferentConstraint(),
                              [j for i in range(block, block + 3) for j in range(i, i + 19, 9)])

    for block in range(27, 34, 3):
        problem.addConstraint(AllDifferentConstraint(),
                              [j for i in range(block, block + 3) for j in range(i, i + 19, 9)])

    for block in range(54, 61, 3):
        problem.addConstraint(AllDifferentConstraint(),
                              [j for i in range(block, block + 3) for j in range(i, i + 19, 9)])

    print(problem.getSolution())
