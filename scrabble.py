
#! needs an import and export module importing pandas for matrix and scrabble_checker function 
#! import also json
#! from the scrabble_dictionary.py
from dotenv import load_dotenv
from scrabble_dictionary import scrabble_checker  
import pandas as pd  
import os
import json

load_dotenv()

scrabble_score_key = json.loads(os.getenv("SCRABLE_SCORE_KEY"))

valid_scrabble_words = scrabble_checker()  

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

def update_scrabble_json(new_data, json_file="./fixtures/scrabble.json"):  # Path ./fixtures/scrabble.json
    if os.path.exists(json_file):
        try:
            with open(json_file, "r") as file:
                existing_data = json.load(file)
        except json.JSONDecodeError:
            print("Warning: scrabble.json is empty or invalid. Initializing as an empty list.")
            existing_data = []
    else:
        existing_data = []

    existing_words = {entry["word"] for entry in existing_data}
    new_data = [entry for entry in new_data if entry["word"] not in existing_words]

    if new_data:
        existing_data.extend(new_data)
        with open(json_file, "w") as file:
            json.dump(existing_data, file, indent=4)
        print(f"{len(new_data)} new word(s) added to scrabble.json fixture")
    else:
        print("No new words to add. All words are already in scrabble.json fixture")

word_scores = get_scrabble_score()
# pd. global function method from pandas library
data_frame = pd.DataFrame(word_scores)
#! print data_frame object (not like Jupiter Notebook)
print(data_frame)

update_scrabble_json(word_scores)

print("Results have been updated in scrabble.json")