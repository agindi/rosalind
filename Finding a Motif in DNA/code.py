import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    with open(os.path.join(__location__, '.\data.dat')) as f:
        lines = f.readlines()
        s = lines[0].strip()
        t = lines[1].strip()
        # I wanna try to do this as a one liner - for the extra flex
        locations = [l+1 for l in range(0, len(s)-len(t)) if s[l:l+len(t)] == t]
        print(" ".join([str(l) for l in locations]))




if __name__ == "__main__":
    main()