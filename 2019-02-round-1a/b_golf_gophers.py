#!/Users/mbukowski/anaconda3/bin/python3

# test locally with following invocation
# python3 b_interactive_runner.py python3 b_testing_tool.py 1 -- ./b_golf_gophers.py 

import fileinput

S = " "

def main():
    # init
    windmills_count = 18
    tests_no, days, max_gophers = -1, -1, -1
    factors = [17, 16, 13, 11, 9, 7, 5]

    # input for the application
    file_input = fileinput.input()

    line = file_input.readline().strip()

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

            # how did state change over night
            state = [int(x) for x in line.split(" ")]
            calc = sum(state)

            # a = b + c
            a.append(calc)
            b.append(calc // f)
            c.append(calc % f)

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

            # TODO this can can additional improvement if we only start from highest factor and go down from there
            # whenever we find a new value which is higher / lower we reset a streak and run work again from scratch
            # with this we will have larger steps ahead
            for i in f_range:
                g[i] = factors[i] * (k[i] + b[i]) + c[i]

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
                    break

                if streak == len(factors):
                    solution = True
                    msg = str(common)
                    break

            if solution:
                print(msg, flush=True)
                line = file_input.readline().strip()

                break

        test_id += 1


if __name__ == "__main__":
    main()