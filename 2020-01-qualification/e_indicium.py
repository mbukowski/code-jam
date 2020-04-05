import fileinput

def main():
    cases_no = 0

    # f = fileinput.input()
    f = open("./2020-01-qualification/input/e_indicium_test.in", "r")
    l1 = f.readline().strip()
    cases_no = int(l1)

    i = 0
    while i < cases_no:
        solution = True

        l2 = f.readline().strip()
        size, trace = [int(x) for x in l2.strip().split(" ")]

        if trace == size + 1:
            solution = False

        if trace == size**2 - 1:
            solution = False

        if solution:
            matrix = build_matrix(size, trace)
            print("Case #%d: POSSIBLE" %(i + 1))
            print_matrix_formatted(matrix)
        else:
            print("Case #%d: IMPOSSIBLE" %(i + 1))

        i += 1

def print_matrix(matrix):
    for row in matrix:
        print(row)

def print_matrix_formatted(matrix):
    for row in matrix:
        s = " ".join([str(x) for x in row])
        print(s)

def build_matrix(size, trace):    
    matrix = []
    diagonal_trace = build_trace(size, trace)

    print("%d %d" %(size, trace))
    print(diagonal_trace)

    # first_element = trace // size
    # for i in range(size):
    #     row = []
    #     x = (first_element - i - 1) % size + 1

    #     for j in range(size):
    #         xx = (x + j - 1) % size + 1
    #         row.append(xx)

    #     matrix.append(row)
    
    return matrix

def build_trace(size, trace):
    diagonal = size*[1]

    while True:
        solution = True

        if (sum(diagonal) == trace):
            el = size*[0]

            # sum up how many times each element was in diagonal trace
            for d in diagonal:
                el[d - 1] += 1

            for e in el:
                if e == size - 1:
                    solution = False
                    break
        else:
            solution = False
        
        # didn't find a solution yet we move to next case
        if not solution:
            for i in reversed(range(size)):
                d = diagonal[i]
                d += 1

                if d > size:
                    d = 1
                    diagonal[i] = d
                else:
                    diagonal[i] = d
                    break

        if solution:
            break
    
    return diagonal



if __name__ == "__main__":
    main()

