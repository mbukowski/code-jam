import fileinput

# iterate through each hill and check if before and after we met condition for peak

folder_name = "2020-kickstart-round-b"
file_name = "a_bike_tour_test.in"


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
        hills_no = int(line)

        line = file_input.readline().strip()
        hills = [int(x) for x in line.strip().split(" ")]

        peaks_no = 0
        for i in range(hills_no - 2):
            prev_peak = hills[i]
            current_peak = hills[i + 1]
            next_peak = hills[i + 2]

            if current_peak > prev_peak and current_peak > next_peak:
                peaks_no += 1

        print("Case #%d: %d" %(test_id + 1, peaks_no))

        test_id += 1


if __name__ == "__main__":
    main()