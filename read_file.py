
with open("persons.txt") as file:
    content = file.read()
    print(content)


#edit

new_text = "\nKevin Kuck, 35 years old, from Heidelberg"

with open("persons.txt", "a") as file:
    file.write(new_text)
