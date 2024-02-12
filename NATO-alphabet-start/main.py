import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

phonetic_alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_alphabet_dict = {row["letter"]: row["code"] for (index, row) in phonetic_alphabet_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name: ").upper()
coded_words = [phonetic_alphabet_dict[letter] for letter in user_input]
print(coded_words)