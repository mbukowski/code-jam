import re

def main():
    regexp = r'(\d*)(N|S|W|E)(.*)'
    content = 'NSS2W56EE125NN'

    # a = int('')
    # print(a)
    # if int(a):
    #     print("0 == True")
    # else: 
    #     print("0 == False")

    while True:
        match_content = re.match(regexp, content)
        
        if match_content:
            g1 = match_content.group(1)
            g2 = match_content.group(2)
            g3 = match_content.group(3)

            print(g1)
            print(g2)
            print(g3)
            print()

            content = g3
            
        else:
            break


if __name__ == "__main__":
    main()