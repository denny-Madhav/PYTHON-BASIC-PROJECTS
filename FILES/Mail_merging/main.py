# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
place_holder = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    # print(names)

with open("./Input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()
    # print(letter_contents)
    for n in names:
        stripped = n.strip()
        new_letter = letter_contents.replace(place_holder, stripped)
        with open(f"./Output/ReadyToSend/letter_for_{n}.txt", mode="w") as completed:
            completed.write(new_letter)

