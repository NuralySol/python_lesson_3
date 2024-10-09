
#! needs a import/export module! against the scrabble checker!
from scrabble_dictionary import scrabble_checker

scrabble_score_key = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
    "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1,
    "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}

valid_scrabble_words = scrabble_checker

def get_scrabble_score():
    user_input = input("Enter word(s) to get Scrabble score(s): ").upper()
    
    words = user_input.replace(',', '').split()
    
    word_scores = []

    for word in words:
        score = 0
        
        is_valid = word.lower() in valid_scrabble_words
        for letter in word:
            if letter in scrabble_score_key:
                score += scrabble_score_key[letter]
        
        if is_valid:
            word_scores.append({"word": word.lower(), "scrabble_score": score})
        else:
            word_scores.append({"word": word.lower(), "scrabble_score": score, "validity": "Not in Scrabble dictionary"})
    
    return word_scores

print(get_scrabble_score())