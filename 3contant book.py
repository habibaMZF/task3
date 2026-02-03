contacts = {
    "Anas": "01012345678",
    "Saja": "01198765432",
    "Yahia": "01234567890"
}

for name in contacts:
    print(name)

search_name = input("Enter a name to search: ")

if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found.")