import fileinput

# so basically it doesn't work like this :D, but it was a good coding practice
# we can build latin squares with all values on the trace without size+1 and size^2-1
def main():
    cases_no = 0

    matrix = [
        [1, 2, 3], 
        [2, 3, 1], 
        [3, 1, 2]]

    matrix = [
        [1, 2, 3, 4], 
        [2, 3, 4, 1], 
        [3, 4, 1, 2], 
        [4, 1, 2, 3]]

    matrix = [
        [1, 2, 3, 4, 5], 
        [2, 3, 4, 5, 1], 
        [3, 4, 5, 1, 2], 
        [4, 5, 1, 2, 3],
        [5, 1, 2, 3, 4]]


    # check init setup
    # print_matrix(matrix)
    # print(trace(matrix))
    row_recurse(matrix, 0)
    column_recurse(matrix, 0)

    # row_combinations(matrix)
    # column_combinations(matrix)

def print_matrix(matrix):
    for row in matrix:
        print(row)

def trace(matrix):
    trace = 0
    i = 0
    for row in matrix:
        trace += row[i]
        i += 1

    return trace

def row_combinations(matrix):
    # check init setup
    # print_matrix(matrix)
    # print(trace(matrix))

    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            matrix_copy = matrix.copy()
            row = matrix_copy[j]
            matrix_copy[j] = matrix_copy[i]
            matrix_copy[i] = row

            # print_matrix(matrix_copy)
            print(trace(matrix_copy))

    print()

def column_combinations(matrix):
    t_matrix = transpose(matrix)

    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            t_matrix_copy = t_matrix.copy()
            row = t_matrix_copy[j]
            t_matrix_copy[j] = t_matrix_copy[i]
            t_matrix_copy[i] = row

            tt_matrix = transpose(t_matrix_copy)
            row_combinations(tt_matrix)

def row_recurse(matrix, start):
    # check init setup
    # print_matrix(matrix)
    # print(trace(matrix))

    for i in range(start, len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            matrix_copy = matrix.copy()
            row = matrix_copy[j]
            matrix_copy[j] = matrix_copy[i]
            matrix_copy[i] = row

            if len(matrix) - j > 2:
                row_recurse(matrix_copy, j + 1)    


            # print("%d: %d %d" %(start, i, j))
            # print_matrix(matrix_copy)
            print(trace(matrix_copy))

    print()

def column_recurse(matrix, start):
    t_matrix = transpose(matrix)

    for i in range(start, len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            t_matrix_copy = t_matrix.copy()
            row = t_matrix_copy[j]
            t_matrix_copy[j] = t_matrix_copy[i]
            t_matrix_copy[i] = row

            tt_matrix = transpose(t_matrix_copy)
            row_recurse(tt_matrix, 0)

            if len(matrix) - j > 2:
                column_recurse(tt_matrix, j + 1)    


def transpose(matrix):
    zip_matrix = zip(*matrix)

    t_matrix = []
    for row in zip_matrix:
        t_matrix.append(row)

    return t_matrix


if __name__ == "__main__":
    main()

