import fileinput
import re

# we use regular expressions to retrieve parts of paths starting from most inner one
# once we have it we compress it to a new format and depending on number of occurances we take that under consideration
# at the end we run compression one more time to make sure everything is in proper format

# regexp for most inner element
regexp_inner = r'(.*)(\d)\((.*?)\)(.*)'

# regexp for handling compressed routes
regexp_compress = r'(\d*)(N|S|E|W)(.*)'

folder_name = "2020-kickstart-round-b"
file_name = "c_robot_path_test.in"


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
        route = line

        # first extract all content from inner parentheses
        while True:
            match_obj = re.match(regexp_inner, route)
            if match_obj:
                route = match_obj.group(1)

                # now we need to compress the whole content to a new string, ex.: NWWEEWSSWS -> N2E4W3S
                count = int(match_obj.group(2))
                content = match_obj.group(3)
                route += compress_route(content, count)

                route += match_obj.group(4)
            else: 
                break

        # finish compressing the route
        route = compress_route(route)
        occur = parse_route(route)

        row = 1
        col = 1

        # N -1
        # S +1
        row -= occur['N']
        row += occur['S']

        row = row % (10 ** 9)
        if row == 0:
            row = 10 ** 9


        # W -1
        # E +1
        col -= occur['W']
        col += occur['E']

        col = col % (10 ** 9)
        if col == 0:
            col = 10 ** 9

        print("Case #%d: %d %d" %(test_id + 1, col, row))

        test_id += 1

# compresses a route to a new format
def compress_route(content, count = 1):
    occur = { 'N': 0, 'S': 0, 'W': 0, 'E': 0 }

    while True:
        match_content = re.match(regexp_compress, content)
        
        if match_content:
            v = match_content.group(1)
            k = match_content.group(2)
            if v:
                occur[k] += int(v)
            else:
                occur[k] += 1
            
            content = match_content.group(3)

        else: 
            break

    route = ''
    for k in occur.keys():
        v = count * occur[k]
        if v > 0:
            if v > 1:
                route += str(v)
            route += k

    return route

# parses route from common format and returns a dict of each direction
def parse_route(content):
    occur = { 'N': 0, 'S': 0, 'W': 0, 'E': 0 }

    while True:
        match_content = re.match(regexp_compress, content)
        
        if match_content:
            v = match_content.group(1)
            k = match_content.group(2)
            if match_content.group(1):
                v = int(match_content.group(1))
            else:
                v = 1

            occur[k] += v    
            
            content = match_content.group(3)

        else: 
            break

    return occur


if __name__ == "__main__":
    main()