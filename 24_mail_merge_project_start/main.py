import os

PLACEHOLDER = "[name]"

this_dir = os.path.dirname(__file__)

with open(f"{this_dir}/Input/Letters/starting_letter.txt") as f:
    letter = f.read()

with open(f"{this_dir}/Input/Names/invited_names.txt") as f:
    name_list = f.readlines()
    name_list = list(map(lambda name: name.replace("\n", ""), name_list))

for name in name_list:
    letter_with_name = letter.replace(PLACEHOLDER, name)
    with open(f"{this_dir}/Output/ReadyToSend/letter_{name}.txt", "w") as f:
        f.write(letter_with_name)
