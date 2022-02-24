import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    with open(os.path.join(__location__, '.\data.dat')) as f:
        lines = f.readlines()
        inputMap = parseFASTA(lines)
        nodes = inputMap.keys()
        edges = list()
        for n1 in nodes:
            for n2 in nodes:
                if n1 == n2:
                    continue
                if(inputMap[n1][-3:] == inputMap[n2][:3]):
                    edges.append((n1, n2))
        print("\n".join([" ".join(e) for e in edges]))


def parseFASTA(inputList):
    outputMap = dict()
    currID = inputList[0][1:-1]
    buffer = ""
    for line in inputList[1:]:
        line = line.strip()
        if (line[0] == '>'):
            outputMap[currID] = buffer + ""
            buffer = ""
            currID = line[1:]
        else:
            buffer = buffer + line
    outputMap[currID] = buffer + ""
    return outputMap


if __name__ == "__main__":
    main()