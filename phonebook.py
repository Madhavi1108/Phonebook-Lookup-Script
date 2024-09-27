n = int(input().strip())  # Number of entries in the phonebook
phonebook = {}

# Store phonebook entries
for _ in range(n):
    entry = input().strip().split()
    name = entry[0]
    phone = entry[1]
    phonebook[name] = phone

# Collect queries (number of queries could be different from n)
queries = []
while True:
    try:
        query = input().strip()
        if query:
            queries.append(query)
        else:
            break
    except EOFError:  # For systems where EOF ends input
        break

# Look up names in the phonebook
for name in queries:
    if name in phonebook:
        print(f"{name}={phonebook[name]}")
    else:
        print("Not found")
