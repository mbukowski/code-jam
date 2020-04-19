from math import factorial as fac

def main():
    fac_list = [1]
    for i in range(10 ** 5):
        fac_list.append(fac_list[-1] * (i + 1))


    # for i in range(10 ** 5):
    #     f = fac(i)
        # print("#%d" %i)
        # print(str(fac(i)))
        # print()

    # f1 = fac(200)
    # f2 = fac(60)
    # f3 = f1 / f2
    # f4 = f1 // f2

    # print("f1: %d" %f1)
    # print("f2: %d" %f2)
    # print("f3: %d" %f3)
    # print("f3: %d" %f3)
    # print("f4: %d" %f4)

    print("done")

if __name__ == "__main__":
    main()