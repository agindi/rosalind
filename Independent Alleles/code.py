import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    with open(os.path.join(__location__, '.\data.dat')) as f:
        line = f.readlines()[0]
        nums = [int(i) for i in line.split(' ')]
        k = nums[0]
        N = nums[1]

        # for any given k and N, there are 
        # God I wish I remembered probability...



        # Let's track the expected number of each allel pair in each generation
        # and then come up with a recurrence
        # Gen 1: E[AA] = .5, E[Aa] = 1, E[aa] = 0.5
        # Gen 2: E[AA] = 1*.5*.5 + 1*1*.5 = .75
        #        E[Aa] = 1*.5*1 + ...

        # formula: E[AA_k] = 2 * E[AA_{k-1}] * P(AA | AA-Aa) + 2 * E[Aa_{k-1}] * P(AA | Aa-Aa)
        #          E[Aa_k] = 2 * E[AA_{k-1}] * P(Aa | AA-Aa) + 2 * E[Aa_{k-1}] * P(Aa | Aa-Aa) + 2 * E[aa_{k-1}] * P(Aa | aa-Aa)
        #          E[aa_k] = 2 * E[Aa_{k-1}] * P(aa | Aa-Aa) + 2 * E[aa_{k-1}] * P(aa | aa-Aa)

        Es = [.5, 1, .5]
        for i in range(1, k):
            nEs = [0,0,0]
            nEs[0] = 2 * (Es[0] * .5 + Es[1] * .25             )
            nEs[1] = 2 * (Es[0] * .5 + Es[1] * .5  + Es[2] * .5)
            nEs[2] = 2 * (             Es[1] * .25 + Es[2] * .5)
            print(nEs)
            Es = nEs

        # Let's find the expected number of Aa Bb descendents and go from there
        # Let H be the event that an offspring is heterozygous for both factors
        # Let Aa be the event that it's het for A, Bb for B.
        # By Mendel's second law, P(H) = P(Aa & Bb) = P(Aa) * P(Bb)
        # Let R_k be the random variable that counts the number of dual hets in the kth generation
        # Note that R_k is binomially distributed ...

        # Let H be the number of Aa Bb alleles in the kth generation
        # E[H] = sum_i=0^n i * P(H = i)
        # = sum_i=0^n i * ( P(Aa = i) x P(Bb = i) )
        


if __name__ == "__main__":
    main()