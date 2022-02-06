import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    with open(os.path.join(__location__, '.\data.dat')) as f:
        line = f.readlines()[0]
        nline = list()
        for c in line[::-1]:
            if c == 'A':
                nline.append('T')
            elif c == 'T':
                nline.append('A')
            elif c == 'C':
                nline.append('G')
            elif c == 'G':
                nline.append('C')
        output = ''.join(nline)
        print(output)




if __name__ == "__main__":
    main()