# Guided Exploration No. 3
# Melanie Henderson

# imports the Python random library
import random

# creates an empty list and assigns it to the variable possible_names
possible_names = []
# creates and opens a new file rap-names-output.txt to be able to write in
outputFile = open('rap-names-output.txt', 'w')
# opens file to read access
with open('rap-names.txt', 'r') as dataFile:
    # using a loop, iterates through and reads each line of file in the dataFile
    for name in dataFile:
        # with each iteration, removes invisible linefeed to the right of each name and appends each name to the possible_names list
        possible_names.append(name.rstrip())
# Asks user how many names to create, converts input to interger and assigns the value to variable named 'count'
count = int(input('How many rap names would you like to create? '))
# Asks user how many parts the name should contain, converts input to an integar and assigns the value to variable named 'parts'
parts = int(input('How many parts should the name contain? '))
# using loop, will iterate for the number of times specified by variable 'count'
for i in range(count):
    # declare an empty list and assign it to name_parts
    name_parts = []
    # using loop, will iterate for the number of times specified by variable 'parts'
    for j in range(parts):
        # with each iteration, it will select a random number between the beginning of the list to end of the list 'possible_names', in order to pick an index value of the possible_names list whose corresponding name will then be appended to the name_parts list.
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
    # Will write in the output file the rap name created, converting the name_parts list into a string and adding a space between each part
    outputFile.write(f"{' '.join(name_parts)}\n")
    # Will print out the rap name
    print(f"{' '.join(name_parts)}")
# Closes the output file
outputFile.close()
