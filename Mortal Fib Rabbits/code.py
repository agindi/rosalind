import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    with open(os.path.join(__location__, '.\data.dat')) as f:
        line = f.readlines()[0]
        nums = line.split(' ')
        n = int(nums[0]) # months
        m = int(nums[1]) # rabbit lifespan

        if(m < 2):
            print('0')
            return

        # let's track both birth numbers and total population size
        pairCounts = [1] * n
        birthCounts = [0] * n
        birthCounts[1] = 1 

        for i in range(2, m):
            birthCounts[i] = pairCounts[i - 2]
            pairCounts[i] = pairCounts[i - 1] + birthCounts[i]

        for i in range(m, n):
            birthCounts[i] = pairCounts[i-2]
            pairCounts[i] = pairCounts[i - 1] + birthCounts[i] - birthCounts[i - m + 1]

        print(pairCounts[n-1])


if __name__ == "__main__":
    main()