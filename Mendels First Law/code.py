import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def main():
    with open(os.path.join(__location__, '.\data.dat')) as f:
        line = f.readlines()[0]
        nums = line.split(' ')
        k = float(nums[0]) #AA
        m = float(nums[1]) #Aa
        n = float(nums[2]) #aa

        # want to compute the probability that a random pairing will produce a dominant phenotyped individual (call event DP)
        # P(DP) = P(AA) + P(Aa)
        # P(AA) = P(AA | 1AA, 2AA)P(1AA, 2AA) + P(AA | 1AA, 2Aa)P(1AA, 2Aa) + P(AA | 1AA, 2aa)P(1AA, 2aa) +
        #         P(AA | 1Aa, 2AA)P(1Aa, 2AA) + P(AA | 1Aa, 2Aa)P(1Aa, 2Aa) + P(AA | 1Aa, 2aa)P(1Aa, 2aa) +
        #         P(AA | 1aa, 2AA)P(1aa, 2AA) + P(AA | 1aa, 2Aa)P(1aa, 2Aa) + P(AA | 1aa, 2aa)P(1aa, 2aa)
        # P(AA) = P(1AA, 2AA) + .5 P(1AA, 2Aa) +
        #         .5 P(1AA, 2AA) + .25 P(1AA, 2Aa) +
        #         P(aa | 1AA, 2AA)P(1AA, 2AA) + P(aa | 1AA, 2Aa)P(1AA, 2Aa) + P(AA | 1aa, 2aa)P(1AA, 2aa)

        # Alternatively...
        # P(DP) = 1 - C_P(DP) = 1 - P(RP) = 1 - P(aa)
        # P(aa) = P(aa | 1Aa, 2Aa)P(1Aa, 2Aa) + P(aa | 1aa, 2Aa)P(1aa, 2Aa) + P(aa | 1Aa, 2aa)P(1Aa, 2aa) + P(aa | 1aa, 2aa)P(1aa, 2aa)
        #       = .25 P(1Aa, 2Aa) + .5 P(1aa, 2Aa) + .5 P(1Aa, 2aa) + P(1aa, 2aa)
        total = k + m + n
        Paa = .25 * ((m / total) * ((m-1)/(total-1)))
        Paa = Paa + .5 * ((n / total) * ((m)/(total-1)))
        Paa = Paa + .5 * ((m / total) * ((n)/(total-1)))
        Paa = Paa + ((n / total) * ((n-1)/(total-1)))
        Pdp = 1 - Paa
        print(Pdp)


if __name__ == "__main__":
    main()