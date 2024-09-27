# Phonebook-Lookup-Script
Overview:
This Python script implements a phonebook system where users can input a set number of phonebook entries and then query names to retrieve the corresponding phone numbers. If a queried name exists in the phonebook, the phone number is printed in a specific format. Otherwise, it indicates that the name is "Not found".

How it Works:
Phonebook Entries:

The user inputs the number of phonebook entries (n).
Each entry consists of a name and a phone number, stored in a dictionary (phonebook), where the name is the key and the phone number is the value.
Queries:

After entering the phonebook data, the user can query names.
The program keeps accepting queries until the input ends (EOF) or a blank line is encountered.
Lookup:

For each queried name, the program checks if it exists in the phonebook.
If the name is found, the name and phone number are printed in the format: name=phone.
If the name is not found, the output is Not found.
