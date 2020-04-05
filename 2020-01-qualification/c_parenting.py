import fileinput

def main():
    cases_no = 0

    f = fileinput.input()
    # f = open("./2020-01-qualification/input/c_parenting_test.in", "r")
    l1 = f.readline().strip()
    cases_no = int(l1)

    i = 0
    while i < cases_no:
        l2 = f.readline().strip()
        activity_size = int(l2)

        # jamie and cameron indicate when they are free
        jamie = -1
        cameron = -1
        activities = []
        activities_dict = {}
        activities_assigned = {}
        activities_output = []

        solution = True

        j = 0
        while j < activity_size:
            l = f.readline().strip()
            activity = [int(x) for x in l.strip().split(" ")]
            activities.append(j)
            activities_dict[j] = activity

            j += 1
        
        # looks there is some magic behind as this below shouldn't work so easily, but as long as it works it's fine
        sorted_activities = []
        for k in sorted(activities_dict, key=activities_dict.get, reverse=False):
            sorted_activities.append(k)

        for a in sorted_activities:
            activity = activities_dict[a]
            if jamie < activity[0]:
                jamie = activity[1] - 1
                activities_assigned[a] = 'J'
            elif cameron < activity[0]:
                cameron = activity[1] - 1
                activities_assigned[a] = 'C'
            else:
                solution = False
                break

        if solution:
            for a in activities:
                activities_output.append(activities_assigned[a])

            print("Case #%d: %s" %(i+1, "".join(activities_output)))
        else:
            print("Case #%d: IMPOSSIBLE" %(i+1))
        i += 1


if __name__ == "__main__":
    main()

