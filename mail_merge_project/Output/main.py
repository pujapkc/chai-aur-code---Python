PLACEHOLDER = "[name]"

with open("./mail_merge_project/input/names/invited_names.txt") as name_file:
    names = name_file.readlines()

#print(names)

with open("./mail_merge_project/input/Letters/starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()

        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

       # print(new_letter)
        with open(f"./mail_merge_project/Output/Ready_to_Send/letter_for_{stripped_name}.docx" ,"w") as completed_letter:
            completed_letter.write(new_letter) 