PLACE_HOLDER = "[name]"

starting_letter_file = "Input/Letters/starting_letter.txt"
invited_names_file = "Input/Names/invited_names.txt"

with open(starting_letter_file, "r") as file:
    letter = file.read()

with open(invited_names_file, "r") as file:
    names = file.readlines()

for name in names:
    stripped_name = name.strip()
    letter_temp = letter.replace(PLACE_HOLDER, name)
    with open(f"Output/ReadyToSend/{name}.txt", "w") as output_file:
        output_file.write(letter_temp)
