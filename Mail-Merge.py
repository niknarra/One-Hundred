# Day 24 - July 3 '24
# Mail Merge
        
# Extracting list of names from the file

with open('./Input/Names/invited_names.txt',mode='r') as listOfNames:
    Names = listOfNames.readlines()

Names = [line.strip() for line in Names]

# Extracting letter content

with open('./Input/Letters/starting_letter.txt',mode='r') as letter:
    content = letter.readlines()

# Creating and Personalizing letter content for each name in the Names list

for name in Names:
    content[0]=content[0].replace('[name]',name)
    with open(f'./Output/ReadyToSend/{name}.txt',mode='w') as finalLetter:
        for line in content:
            finalLetter.write(line)
    content[0]=content[0].replace(name,'[name]')
