import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    with open(os.path.join(__location__, '.\data.dat')) as f:
        line = f.readlines()[0]
        counters = dict()
        for c in line:
            if c == '\n':
                continue
            if c in counters.keys():
                counters[c] += 1
            else:
                counters[c] = 1
        print(str(counters['A']) + ' ' + str(counters['C']) + ' ' + str(counters['G']) + ' ' + str(counters['T']))




if __name__ == "__main__":
    main()