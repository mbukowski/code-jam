keys = ( \
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', \
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
    'U', 'V', 'W', 'X', 'Y', 'Z' )

import fileinput

E = ''
S = ' '
T = '\t'

def main():
    # init
    # folder_name = "2019-02-round-1a/input/"
    folder_name = "input/"
    file_name = "c_alien_rhyme_test.in"
    tests_no = -1

    file_input = open(folder_name + file_name, "r")
    # file_input = fileinput.input()

    line = file_input.readline().strip()
    tests_no = int(line)

    test_id = 0
    while test_id < tests_no:
        input_words = []
        words = []
        accents = []

        line = file_input.readline().strip()
        words_no = int(line)

        for word_no in range(words_no):
            word = file_input.readline().strip()
            input_words.append(E.join(reversed(word)))

        print(input_words)
        for w in sorted(input_words):
            words.append(tuple(w))
            print(w)

        extract_accents(words, accents, 0)

        print("Case #%d: %d" %(test_id + 1, 2 * len(accents)))

        test_id += 1


    file_input.close()

def extract_accents(words, accents, accent_id):
    count = len(words)
    new_accent_id = accent_id + 1

    # we have more than 3 items and it may be good to continue splitting them
    if count > 3:
        new_words = []
        left_words = []
        word_count = 1
        current_char = words[0][accent_id]


        for word in words:
            extract = False

            if word[accent_id] == current_char:
                if len(word) == new_accent_id:
                    left_words.append(word)
                else:
                    new_words.append(word)

            else:
                extract = True

            if extract or word_count == count:
                extract_accents(new_words, accents, new_accent_id)
                left_words.append(new_words)

                # accent = word[0:new_accent_id]

                if extract:
                    current_char = word[accent_id]
                    new_words = []
                    new_words.append(word)


            # this is the last word
            if word_count == count:

                # if not accent in accents:
                    # if len(left_words) > 1:



                # char = w[accent_id]
                # new_words = []
                # 


        # we finished above loop but we still have last items to go through
        extract_accents(new_words, accents, accent_id + 1)    
        left_words.append(new_words)

        #     a = 1
        #     #


        # print("1")
    # we have either 2 and 3 and this is the end of the journey, find one accent and go back
    elif count > 1:
        accent = word[0:new_accent_id]
        if not accent in accents:
            accents.append(accent)
            del(words[:2])

    # nothing to see here, go back
    elif count == 1:
        print("3")



if __name__ == "__main__":
    main()