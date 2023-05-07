"""Given a word, compute the Scrabble score for that word.
Letter Values
You'll need these:
Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10"""

points = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    6: [],
    7: [],
    8: ["J", "X"],
    9: [],
    10: ["Q", "Z"]
}

def score(word):
    word = word.upper()
    score = []
    for letter in word:
        for key, value in points.items():
            if letter in value:
                score.append(key)
    return sum(score)       