"""An anagram is a rearrangement of letters to form a new word: for example "owns" is an anagram of "snow". A word is not its own anagram: for example, 
"stop" is not an anagram of "stop".
Given a target word and a set of candidate words, this exercise requests the anagram set: the subset of the candidates that are anagrams of the target.
The target and candidates are words of one or more ASCII alphabetic characters (A-Z and a-z). Lowercase and uppercase characters are equivalent: 
for example, "PoTS" is an anagram of "sTOp", but StoP is not an anagram of sTOp. The anagram set is the subset of the candidate set that are anagrams of the target 
(in any order). Words in the anagram set should have the same letter case as in the candidate set.
Given the target "stone" and candidates "stone", "tones", "banana", "tons", "notes", "Seton", the anagram set is "tones", "notes", "Seton"."""

def find_anagrams(word, candidates):
    word_lower = word.lower()
    candidates_lower = [char.lower() for char in candidates]
    
    # removes any words in candidates list that is the same word
    candidates_lower_cp = candidates_lower.copy()
    for chars in candidates_lower_cp:
        if word_lower == chars:
            candidates_lower_cp.remove(chars)
    
    # sorts the word and the words in the candidates list
    new_word = "".join(sorted(word_lower))
    new_candidates = []
    for words in candidates_lower_cp:
        i = "".join(sorted(words))
        new_candidates.append(i)
    
    # makes a list of the anagram words
    indexes = []
    for i, j in enumerate(new_candidates):
        if j == new_word:
            indexes.append(i)
    result = []
    for numbers in indexes:
        anagram = candidates_lower_cp[numbers]
        index_num = candidates_lower.index(anagram)
        result.append(candidates[index_num])
         
    return result       