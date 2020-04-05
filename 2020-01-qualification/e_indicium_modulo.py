import fileinput

# solution based on invalid indicium experiment
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

        if trace % size != 0:
            solution = False
        
        if trace > size**2:
            solution = False

        if trace < size:
            solution = False
    
        if size < 2:
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

    first_element = trace // size
    for i in range(size):
        row = []
        x = (first_element - i - 1) % size + 1

        for j in range(size):
            xx = (x + j - 1) % size + 1
            row.append(xx)

        matrix.append(row)
    
    return matrix


if __name__ == "__main__":
    main()

