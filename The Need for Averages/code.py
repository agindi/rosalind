import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    with open(os.path.join(__location__, '.\data.dat')) as f:
        line = f.readlines()[0]
        nums = [int(i) for i in line.split(' ')]

        # each element in nums represents the number of a type of coupling
        # each type of coupling has a different probability of yielding an offspring with the dominant phenotype
        # P(DP | AA-AA) = 1
        # P(DP | AA-Aa) = 1
        # P(DP | AA-aa) = 1
        # P(DP | Aa-Aa) = .75
        # P(DP | Aa-aa) = .5
        # P(DP | aa-aa) = 0
        # Assume that every couple has two offspring and that each of these offspring's genotypes are independent
        # Then, E[|DP| | x] = 2 * P(DP | x) * n_x
        # So E[|DP|] = ...
        print(2 * (nums[0] + nums[1] + nums[2] + .75 * nums[3] + .5 * nums[4]))
        


if __name__ == "__main__":
    main()