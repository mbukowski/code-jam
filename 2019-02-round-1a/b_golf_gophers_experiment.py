import itertools
import random

S = " "

def main():
    # init
    gophers_count = 100
    windmills_count = 18
    factors = [17, 13, 11, 7, 5, 3, 2]
    seed = 1951

    a, b, c = [], [], []

    random.seed(seed)

    # generate input data for each night
    for f in factors:
        windmills = [f] * windmills_count

        state = night_check(windmills, gophers_count)
        calc = sum(state)

        # a = b + c
        a.append(calc)
        b.append(calc // f)
        c.append(calc % f)

        print(windmills)
        print(state)
        print("%d = %d * %d + %d\n" %(a[-1], f, b[-1], c[-1]))
        
    # check k and l from following equations, we search for lowest k and l
    # f1 * k + a1 = f2 * l + a2, ex.:
    # 17 * k + a1 = 13 * l + a2
    # 13 * k + a1 = 11 * l + a2 ...
    # later we store results in k array
    f_range = range(len(factors))
    kl = [[0 for i in f_range] for j in f_range]
    for i, j in itertools.product(f_range, f_range):
        f1 = factors[i]
        f2 = factors[j]

        # a = b + c
        a1, a2 = a[i], a[j]
        b1, b2 = b[i], b[j]
        c1, c2 = c[i], c[j]

        lowest_common = 0
        k = 0
        l = 0
        while True:
            g1 = f1 * (k + b1) + c1
            g2 = f2 * (l + b2) + c2
            lowest_common = max(g1, g2)

            if g1 == g2:
                kl[i][j] = str([k, l, lowest_common])
                break
            elif g1 < g2:
                step = (g2 - g1) // f1
                k += max(step, 1) 
            elif g2 < g1:
                step = (g1 - g2) // f2
                l += max(step, 1)
            
            if g1 > gophers_count or g2 > gophers_count:
                print("Error didn't find common")
                break

    print_array(kl)

def night_check(windmills, gophers_count):
    result = [0] * len(windmills)    

    for i in range(gophers_count):
        index = random.randint(0, len(windmills) - 1)
        result[index] = (result[index] + 1) % windmills[index]

    return result

def print_array(arr):
    for row in arr:
        s = S.join([str(elem) for elem in row])
        print(s)

if __name__ == "__main__":
    main()