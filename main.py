with open('./Input/Names/invited_names.txt') as names:
    names_of_people = names.readlines()


with open('./Input/Letters/starting_letter.docx') as letters:
    heading = letters.readline()
    letter = letters.readlines()
    for person in names_of_people:
        new_name = person.strip('\n')
        new_location = f"./Output/ReadyToSend/letter_for{new_name}.docx"
        #
        with open(new_location, 'a') as file:
            new_heading = heading.replace(heading, f'Dear {new_name}')
            file.write(new_heading)
            for line in letter:
                file.write(line)