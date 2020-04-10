import fileinput

T = "\t"
S = " "

def main():
    tests_no = 0

    folder_name = "2019-02-round-1a"
    file_name = "a_pylons_test.in"

    f = open("./" + folder_name + "/input/" + file_name, "r")
    # f = open("./input/" + file_name, "r")
    # f = fileinput.input()

    l1 = f.readline().strip()
    tests_no = int(l1)

    i = 0
    while i < tests_no:
        solution = True

        l2 = f.readline().strip()
        r, c = [int(x) for x in l2.split(" ")]

        if (r == 2 and c < 5) or (c == 2 and r < 5) or (r == 3 and c == 3):
            solution = False
        else:
            path = find_path(r, c)
        
        if solution:
            print("Case #%d: POSSIBLE" %(i + 1))
            for p in path:
                print(S.join([str(e) for e in p]))
        else:
            print("Case #%d: IMPOSSIBLE" %(i + 1))

        i += 1


def find_path(r, c):
    visited = [[0 for j in range(c)] for i in range(r)]
    path = []
    max = r * c
    id = 1

    x = 0
    y = 0

    while True:
        visited[x][y] = id
        path.append([x + 1, y + 1])
        # print_array(visited)
        # print()

        if id == max:
            return path

        x = (x + 1) % r
        # back to first row, we take next unused column
        if (x == 0):
            y = id // r
        # we are in other rows and here we have to distinguish if row is even or odd
        # in even we add 2 from past column and in odd we substract 2
        elif (x % 2 == 1):
            y = (y + 2) % c
        elif (x % 2 == 0):
            y = (y - 2 + c) % c     

        id += 1

def print_array(arr):
    for row in arr:
        print(T.join([str(elem) for elem in row]))


if __name__ == "__main__":
    main()