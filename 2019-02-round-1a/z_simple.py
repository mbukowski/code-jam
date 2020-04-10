import itertools

factors = [17, 13, 11, 7, 5, 3, 2]

# for f1, f2 in itertools.product(factors, factors):
#     print(str(f1) + " " + str(f2))

f_range = range(len(factors))
for i, j in itertools.product(f_range, f_range):
    f1 = factors[i]
    f2 = factors[j]

    print(str(i) + " " + str(j))
    # print(str(f1) + " " + str(f2))
