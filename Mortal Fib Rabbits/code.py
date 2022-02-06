import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    with open(os.path.join(__location__, '.\data.dat')) as f:
        line = f.readlines()[0]
        nums = line.split(' ')
        n = int(nums[0]) # months
        k = int(nums[1]) # rabit pairs per litter

        # In any given month, k new rabit pairs are born for each rabbit pair that
        # was alive 2 months prior.
        # We add these new rabit pairs to the total for the previous month to get
        # the new total for that month

        pairCounts = [1] * n

        for i in range(2, n):
            pairCounts[i] = pairCounts[i-1] + k * pairCounts[i-2]
        
        print(pairCounts[n-1])




if __name__ == "__main__":
    main()