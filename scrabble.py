
#! needs an import and export module importing pandas for matrix and scrabble_checker function 
#! import also json
#! from the scrabble_dictionary.py
from scrabble_dictionary import scrabble_checker
import pandas as pd
import os
import json

# changed it to a tuple a more appropriate data structure for scores
scrabble_score_key = (
    ("A", 1),
    ("B", 3),
    ("C", 3),
    ("D", 2),
    ("E", 1),
    ("F", 4),
    ("G", 2),
    ("H", 4),
    ("I", 1),
    ("J", 8),
    ("K", 5),
    ("L", 1),
    ("M", 3),
    ("N", 1),
    ("O", 1),
    ("P", 3),
    ("Q", 10),
    ("R", 1),
    ("S", 1),
    ("T", 1),
    ("U", 1),
    ("V", 4),
    ("W", 4),
    ("X", 8),
    ("Y", 4),
    ("Z", 10),
)

# conversion back to dict. using the global function
scrabble_score_dict = dict(scrabble_score_key)

valid_scrabble_words = scrabble_checker()

# Function get_scrabble_score to check against the dict.
def get_scrabble_score():
    user_input = input("Enter word(s) to get Scrabble score(s): ").upper()
    words = user_input.replace(",", "").split()
    word_scores = []

    for word in words:
        score = 0
        is_valid = word.lower() in valid_scrabble_words

        # Word calculator for each word based on the scrabble_score_dict
        for letter in word:
            if letter in scrabble_score_dict:
                score += scrabble_score_dict[letter]

        # Append the result to word_scores empty list
        if is_valid:
            word_scores.append({"word": word.lower(), "scrabble_score": score})
        else:
            word_scores.append(
                {
                    "word": word.lower(),
                    "scrabble_score": score,
                    "validity": "Not in Scrabble dictionary",
                }
            )

    return word_scores

#! Update and keep the scrabble fixture with scores, etc. (static file)
def update_scrabble_json(new_data, json_file="./fixtures/scrabble.json"): # Path ./fixtures/scrabble.json
    if os.path.exists(json_file):
        with open(json_file, "r") as file:
            existing_data = json.load(file)
    else:
        existing_data = []

    existing_data.extend(new_data)

    # Write the updated data back to the JSON file in dict. format 
    with open(json_file, "w") as file:
        json.dump(existing_data, file, indent=4)

# Get scrabble word scores as a list of dictionaries
word_scores = get_scrabble_score()

#! pd global function of pandas matrix library
df = pd.DataFrame(word_scores)

# Matrix pandas object print (different from Jupyter Notebook where you can just call the object here needs a print)
print(df)

# Update the scrabble.json file with new results
update_scrabble_json(word_scores)

# Print success message for debugging purposes
print("Results have been updated in scrabble.json")