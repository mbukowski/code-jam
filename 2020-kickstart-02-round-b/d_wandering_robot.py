import fileinput
import math 

from math import factorial as fac
from fractions import Fraction

T = "\t"
S = " "

# TODO not completed need to work on these logarithms
# some discussions
# https://codeforces.com/blog/entry/76242


def main():
    tests_no = 0

    folder_name = "2020-kickstart-round-b"
    file_name = "d_wandering_robot_test.in"

    file_input = open("./" + folder_name + "/input/" + file_name, "r")
    # file_input = open("./input/" + file_name, "r")
    # file_input = fileinput.input()

    line = file_input.readline().strip()
    tests_no = int(line)

    # fac_list = []
    # for i in range(301):
    #     fac_list.append(fac(i))

    # fac_list = [1]
    # for i in range(10 ** 5):
    #     fac_list.append(fac_list[-1] * (i + 1))        

    test_id = 0
    while test_id < tests_no:
        line = file_input.readline().strip()
        w, h, l, u, r, d = [int(x) for x in line.strip().split(" ")]

        probability = Fraction(0, 1)
        if not (w == 1 or h == 1):
            # 01 center
            if l > 1 and u > 1 and r < w and d < h:
                # above
                for i in range(u - 1):
                    # p = 0.5 ** i * 0.5 ** r
                    # p = binomial2(r, i) * (0.5 ** i) * (0.5 ** r)
                    bi = binomial(r, i)
                    p1 = 0.5 ** i
                    p2 = 0.5 ** r
                    p = bi * p1 * p2

                    # print("BI %d" %bi)
                    # print("I %d" %i)
                    # print("P1 %f" %p1)
                    # print("R %d" %r)
                    # print("P2 %f" %p2)
                    # print("P %f" %p)
                    # print()

                    probability += Fraction(p)

                    # p = Fraction(binomial(r, i), 1) * pow_fraction(1, 2, i) * pow_fraction(1, 2, r)
                    # probability += p
                    

                # under
                for i in range(l - 1):
                    # p = 0.5 ** i * 0.5 ** d
                    # p = binomial2(d, i) * (0.5 ** i) * (0.5 ** d)
                    p = Fraction(binomial(d, i), 1) * pow_fraction(1, 2, i) * pow_fraction(1, 2, d)
                    probability += p
                
            # 02 above 
            if l > 1 and u > 1 and r < w and d == h:
                for i in range(u - 1):
                    p = Fraction(binomial(r, i), 1) * pow_fraction(1, 2, i) * pow_fraction(1, 2, r)
                    probability += p

            # 03 under
            if l > 1 and u > 1 and r == w and d < h:
                for i in range(l - 1):
                    p = Fraction(binomial(d, i), 1) * pow_fraction(1, 2, i) * pow_fraction(1, 2, d)
                    probability += p

            # # 04 fail
            # if l > 1 and u > 1 and r == w and d == h:
            #     probability += 0.0

            # 05 under
            if l > 1 and u == 1 and r < w and d < h:
                for i in range(l - 1):
                    p = Fraction(binomial(d, i), 1) * pow_fraction(1, 2, i) * pow_fraction(1, 2, d)
                    probability += p

            # # 06 fail
            # if l > 1 and u == 1 and r < w and d == h:
            #     probability += 0.0

            # 07 under
            if l > 1 and u == 1 and r == w and d < h:
                for i in range(l - 1):
                    p = Fraction(binomial(d, i), 1) * pow_fraction(1, 2, i) * pow_fraction(1, 2, d)
                    probability += p

            # # 08 fail
            # if l > 1 and u == 1 and r == w and d == h:
            #     probability += 0.0

            # 09 above
            if l == 1 and u > 1 and r < w and d < h:
                for i in range(u - 1):
                    p = Fraction(binomial(r, i), 1) * pow_fraction(1, 2, i) * pow_fraction(1, 2, r)
                    probability += p
                
            # 10 above
            if l == 1 and u > 1 and r < w and d == h:
                for i in range(u - 1):
                    p = Fraction(binomial(r, i), 1) * pow_fraction(1, 2, i) * pow_fraction(1, 2, r)
                    probability += p

            # # 11 fail
            # if l == 1 and u > 1 and r == w and d < h:
            #     probability += 0.0

            # # 12 fail
            # if l == 1 and u > 1 and r == w and d == h:
            #     probability += 0.0

            # # 13 fail
            # if l == 1 and u == 1 and r < w and d < h:
            #     probability += 0.0

            # # 14  fail
            # if l == 1 and u == 1 and r < w and d == h:
            #     probability += 0.0

            # # 15 fail
            # if l == 1 and u == 1 and r == w and d < h:
            #     probability += 0.0

            # # 16 fail
            # if l == 1 and u == 1 and r == w and d == h:
            #     probability += 0.0

        print("Case #%d: %.5f" %(test_id + 1, probability))

        test_id += 1

def binomial(n, k):
    try:
        binom = fac(n) // fac(k) // fac(n - k)
    except ValueError:
        binom = 0
    return binom

def binomial_mem(n, k, fac_list):
    try:
        binom = fac_list[n] // fac_list[k] // fac_list[n - k]
    except ValueError:
        binom = 0
    return binom


# [n!] / [k! * (n - k)!]
def binomial2(n, k):
    r1 = 1
    for i in range(k + 1, n + 1, 1):
        r1 *= i

    r2 = 1
    for i in range(1, n - k + 1, 1):
        r2 *= i

    r = r1 // r2
    return r

def pow_fraction(n, d, p):
    f = Fraction(n, d)

    r = Fraction(1, 1)
    for i in range(p):
        r *= f

    return r


if __name__ == "__main__":
    main()