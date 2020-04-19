import fileinput

# we start from last day and we check what is a last possible day where we can take that bus
# then we move to a previous one if that one can be taken on the same day we remember it, otherwise we find earlier day
# and with that we move to a first possible one

folder_name = "2020-kickstart-round-b"
file_name = "b_bus_routes_test.in"


def main():
    tests_no = 0

    file_input = open("./" + folder_name + "/input/" + file_name, "r")
    # file_input = open("./input/" + file_name, "r")
    # file_input = fileinput.input()

    line = file_input.readline().strip()
    tests_no = int(line)

    test_id = 0
    while test_id < tests_no:
        line = file_input.readline().strip()
        routes_no, days_no = [int(x) for x in line.strip().split(" ")]

        line = file_input.readline().strip()
        occurs = [int(x) for x in line.strip().split(" ")]

        first_day = days_no
        for o in reversed(occurs):
            a = first_day // o
            day = a * o
            first_day = min(day, first_day)

        print("Case #%d: %d" %(test_id + 1, first_day))

        test_id += 1


if __name__ == "__main__":
    main()