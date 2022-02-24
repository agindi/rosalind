import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    with open(os.path.join(__location__, '.\data.dat')) as f:
        lines = f.readlines()
        inputMap = parseFASTA(lines)
        maxItem = max(inputMap.items(), key = lambda k : computeGCContent(k[1]))
        print(maxItem[0])
        print(round(100*computeGCContent(maxItem[1]), 4))

def computeGCContent(seq):
    compiler = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in seq:
        compiler[base] += 1
    return (compiler['C'] + compiler['G']) / sum(compiler.values())

def parseFASTA(inputList):
    outputMap = dict()
    currID = inputList[0][:-1]
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