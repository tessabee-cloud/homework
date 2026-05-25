
#1

def analyze_file(filename):
    with open(filename, "r", encoding='utf-8') as f:
        content = f.read()

        lines = content.splitlines()

        words = content.split()

        chars = len(content)

    print('lines:', len(lines))
    print('words:', len(words))
    print('characters (including spaces):', chars)


analyze_file('data.txt')


#2
data = open('journal.txt', 'a')
while True:
    text  = str(input("input your text or 'exit' to exit: "))
    data.writelines(text + '\n')
    if text == 'exit':
        break


#3

import csv

filtered = []
with open('products.csv', 'r', newline='') as f:
    reader = csv.DictReader(f, delimiter=',')
    writer = csv.DictWriter(data, fieldnames=reader.fieldnames)
    writer.writeheader()
    header = next(reader)
    price_min = float(input("input minimal price: "))

    for row in reader:

        price = float(row['price'])
        if price >= price_min:
            filtered.append(row)


with open('flitered_product.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=filtered[0].keys())

    writer.writeheader()
    writer.writerows(filtered)


#4

#4.1
with open('contacts.csv', 'r', newline='') as f:
    reader = csv.DictReader(f, delimiter=',')

    for contact in reader:
        print(contact)


#4.2
name= input('enter name:')
phone = input('enter phone number:')
email = input('enter email:')

new_contact = {
    'name': name,
    'phone': phone,
    'email': email
}

with open('contacts.csv', 'a', newline='') as f:
    fieldnames = ['name', 'email', 'phone']

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(new_contact)
print('contact added')

#4.3

search_name = input('enter name to search:')

with open('contacts.csv', 'r', newline='') as f:
    reader = csv.DictReader(f, delimiter=',')

    found = False

    for contact in reader:
        if contact['name'].lower() == search_name.lower():
            print(contact)
            found  = True

    if not found:
        print('contact not found')


#4.4

delete_name = input('enter name to delete:')

contacts = []
found = False

with open('contacts.csv', 'r', newline='') as f:
    reader = csv.DictReader(f, delimiter=',')

    for contact in reader:
        if contact['name'].lower() == delete_name.lower():
            found = True
        else:
            contacts.append(contact)

if found:

    with open('contacts.csv', 'w', newline='') as f:
        fieldnames = ['name', 'email', 'phone']

        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(contacts)
        print('contact deleted')

else:
    print('there is no contact with this name')





