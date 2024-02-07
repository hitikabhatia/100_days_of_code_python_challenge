STARTING_LETTER_FILE_PATH = "./Input/Letters/starting_letter.txt"
NAMES_FILE_PATH = "./Input/Names/invited_names.txt"
OUTPUT_PATH = "./Output/ReadyToSend/{user_name}.txt"

# let's first read the content of the letter from the file.
letter_template = []
with open(file=STARTING_LETTER_FILE_PATH, mode="r") as letter_file:
    letter_template = letter_file.readlines()

# reading the names of the invited people from file and saving in a list
invitees_list = []
with open(file=NAMES_FILE_PATH, mode="r") as invited_names:
    invitees_list = invited_names.readlines()

# Removing \n from the names in the list.
for name_index in range(0, len(invitees_list)):
    if "\n" in invitees_list[name_index]:
        invitees_list[name_index] = invitees_list[name_index].strip("\n")

# Writing all the letters and saving to the new files.
letter = []
for each_name in invitees_list:
    outfile_path = OUTPUT_PATH.replace("{user_name}", each_name)
    letter = letter_template[:]
    letter[0] = letter[0].replace("[name]", each_name)
    with open(file=outfile_path, mode="w") as new_letter_file:
        new_letter_file.writelines(letter)