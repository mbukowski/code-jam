import fileinput

def main():
    cases_no = 0

    f = fileinput.input()
    # f = open("./2020-01-qualification/input/b_nesting_depth_test_02.in", "r")
    # f = open("./input/b_nesting_depth_test_02.in", "r")
    l1 = f.readline().strip()
    cases_no = int(l1)

    i = 0
    while i < cases_no:
        l2 = f.readline().strip()
        arr1 = [x for x in l2]
        arr2 = arr1.copy()

        # iterate from 9 to 0, without looking at 0 as we don't need parentheses around that 
        for n in range(9, 0, -1):
            # how many open how many closed parentheses
            count = 0

            # where did we open last time parentheses
            opened_index = -1

            # where exactly are we right now
            current_index = 0

            # iterate through arr
            for c in arr1:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                else:
                    val = int(c)
                    if val > n:
                        # we need to add few before
                        if count == val - n:
                            arr2.insert(current_index, '(')
                            current_index += 1
                            count += 1

                    elif val == n:
                        if count == val - n:
                            arr2.insert(current_index, '(')
                            current_index += 1
                            count += 1
                    
                    elif val < n:
                        while count > 0:
                            arr2.insert(current_index, ')')
                            current_index += 1
                            count -= 1

                current_index += 1

            while count > 0:
                arr2.insert(current_index, ')')
                current_index += 1
                count -= 1

            arr1 = arr2.copy()

        print("Case #%d: %s" %(i+1, "".join(arr1)))
        i += 1


if __name__ == "__main__":
    main()

