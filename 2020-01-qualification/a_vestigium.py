import fileinput

def main():
    cases_no = 0

    f = fileinput.input()
    # f = open("./2020-01-qualification/input/a_vestigum_test.in", "r")
    # f = open("./input/a_vestigum_test.in", "r")
    l1 = f.readline()
    cases_no = int(l1)

    i = 0
    while i < cases_no:
        l2 = f.readline()
        matrix_size = int(l2)
        matrix = []

        trace = 0
        rows_repeat = 0
        cols_repeat = 0

        j = 0
        while j < matrix_size:
            l = f.readline()
            row = [int(x) for x in l.strip().split(" ")]
            sorted_row = sorted(row)
            matrix.append(row)

            trace += row[j]

            if sum(row) != arithmetic_sum_n(matrix_size):
                rows_repeat += 1
            elif has_duplicates(sorted_row):
                rows_repeat += 1

            j += 1

        t_matrix = zip(*matrix) 
        for col in t_matrix:
            sorted_col = sorted(col)
            if sum(col) != arithmetic_sum_n(matrix_size):
                cols_repeat += 1
            elif has_duplicates(sorted_col):
                cols_repeat += 1
        
        print("Case #%d: %d %d %d" %(i+1, trace, rows_repeat, cols_repeat))

        i += 1

def arithmetic_sum_n(n):
    return arithmetic_sum(1, n, n)

def arithmetic_sum(start, end, no):
    return ((start + end) * no) / 2

def has_duplicates(arr):
    size = len(arr)
    for i in range(size - 1):
        if (arr[i] == arr[i + 1]):
            return True

    return False

if __name__ == "__main__":
    main()

