import string
import random

def generate_card(length=7):
    genes = random.choices(string.ascii_uppercase[:10], k=length)  # Usa solo lettere A-J per semplicità
    return ''.join(genes)


def createDP(a_len, b_len):
    return [[0 for _ in range(b_len + 1)] for _ in range(a_len + 1)]

def LCS(a, b):
    dp = createDP(len(a), len(b)) #creating dynamic programming table
    for i in range(1, len(a) + 1): 
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]: #if equal character
                dp[i][j] = dp[i-1][j-1] + 1 #expand the dp by one removing last character from both strings
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) #finds the best choice if remove last from string a or b using optimal substructure
    return dp


def reconstruct_LCS(dp, a, b):
    i, j = len(a), len(b) #start from right bottom of the dp
    lcs = []

    while i > 0 and j > 0:
        if a[i-1] == b[j-1]: #if characters are equal this are part of the lcs
            lcs.append(a[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]: #finding the optimal subproblem and traversing the dp
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs)) #inverting subsequence

def evolve_cards(card1, card2):
    print(f" Card 1 DNA: {card1}")
    print(f" Card 2 DNA: {card2}")

    dp = LCS(card1, card2)
    new_card = reconstruct_LCS(dp, card1, card2)

    print(f"\n Evolved Card DNA (LCS): {new_card}")
    print(f"Power Level: {len(new_card)} abilities inherited!\n")

def main():
    print(" Welcome to the Card Evolution Game! \n")
    card1 = generate_card()
    card2 = generate_card()

    evolve_cards(card1, card2)

if __name__ == "__main__":
    main()

