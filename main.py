with open('./input/Names/invited_names.txt') as names:
    list_of_names = names.readlines()

placeholder = '[name]'

with open('./input/Letters/starting_letter.docx') as letters:
    letter = letters.read()
    print(letters)
    for person in list_of_names:
        new_name = person.strip('\n')
        new_letter = letter.replace(placeholder,new_name)
        # print(new_letter)