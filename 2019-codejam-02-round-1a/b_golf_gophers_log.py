#!/Users/mbukowski/anaconda3/bin/python3

import fileinput

S = " "
log_enabled = True

# folder_name = "2019-02-round-1a/output"
folder_name = "output/"
file_name = "b_golf_gophers.out"

def main():
    # init
    windmills_count = 18
    tests_no, days, max_gophers = -1, -1, -1
    factors = [17, 16, 13, 11, 9, 7, 5]

    # debug
    out = open_log()

    # input for the application
    file_input = fileinput.input()

    line = file_input.readline().strip()
    log(out, "IN: %s\n" %line)

    # read input parameters
    tests_no, days, max_gophers = [int(x) for x in line.split(" ")]

    test_id = 0
    while test_id < tests_no:     
        a, b, c = [], [], []

        # collect data
        for f in factors:
            windmills = [f] * windmills_count
            msg = S.join([str(e) for e in windmills])

            print(msg, flush=True)
            line = file_input.readline().strip()
            log(out, "#%d OUT: %s" %(test_id, msg))
            log(out, "#%d IN: %s" %(test_id, line))

            # how did state change over night
            state = [int(x) for x in line.split(" ")]
            calc = sum(state)

            # a = b + c
            a.append(calc)
            b.append(calc // f)
            c.append(calc % f)

            log(out, "#%d F: %d" %(test_id, f))
            log(out, "#%d A: %d" %(test_id, a[-1]))
            log(out, "#%d B: %d" %(test_id, b[-1]))
            log(out, "#%d C: %d" %(test_id, c[-1]))
            log(out)
        
        # check k and l from following equations, we search for lowest k and l
        # f1 * k + a1 = f2 * l + a2, ex.:
        # 17 * k + a1 = 13 * l + a2
        # 13 * k + a1 = 11 * l + a2 ...
        # ok we iterate from bottom to top and check where we find the smallest common denominator it will go one by one, 
        # and we can adjust as we go
        # each of the step must equal to common last time and then streak must be equal to number of factors
        f_range = range(len(factors))
        g = [0] * len(factors)
        k = [0] * len(factors)
        common = 0
        streak = 0
        while True:
            solution = False
            result = "dummy"

            for i in f_range:
                g[i] = factors[i] * (k[i] + b[i]) + c[i]

                log(out, "#%d G: %s" %(test_id, S.join([str(x) for x in g])))
                log(out, "#%d K: %s" %(test_id, S.join([str(x) for x in k])))

                if g[i] == common:
                    streak += 1
                elif g[i] > common:
                    streak = 0
                    common = g[i]
                elif g[i] < common:
                    streak = 0
                    step = (common - g[i]) // factors[i]
                    k[i] += max(step, 1)

                if g[i] > max_gophers:
                    solution = True
                    result = "-1"
                    log(out, "Error didn't find common")
                    break

                if streak == len(factors):
                    solution = True
                    msg = str(common)
                    log(out, "Reached a minimum streak")
                    break

            if solution:
                print(msg, flush=True)
                line = file_input.readline().strip()

                log(out, "#%d OUT: %s" %(test_id, msg))
                log(out, "#%d IN: %s" %(test_id, line))
                log(out, "****************************************")
                log(out)

                break

        test_id += 1

    close_log(out)


def open_log():
    if log_enabled:
        out = open(folder_name + file_name, "w")
        return out

def close_log(out):
    if log_enabled:
        out.close()

def log(out, s=""):
    if log_enabled:
        out.write(s + "\n")

# function to log 2d arrays
def log_array(out, arr):
    for row in arr:
        s = S.join([str(elem) for elem in row])
        log(out, s)


if __name__ == "__main__":
    main()