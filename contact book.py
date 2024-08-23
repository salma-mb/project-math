class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
                with open(self.filename, 'r') as file:
                    contacts = []
                    for line in file:
                        name, phone, email = line.strip().split(',')
                        contacts.append(Contact(name, phone, email))
                    return contacts
        except FileNotFoundError:
                return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phone},{contact.email}\n")

    def add_contact(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()

    def edit_contact(self, index, name, phone, email):
        self.contacts[index] = Contact(name, phone, email)
        self.save_contacts()

    def delete_contact(self, index):
        del self.contacts[index]
        self.save_contacts()

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

def main():
    contact_book = ContactBook('contacts.txt')
    while True:
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            index = int(input("Enter contact index: "))
            name = input("Enter new name: ")
            phone = input("Enter new phone: ")
            email = input("Enter new email: ")
            contact_book.edit_contact(index, name, phone, email)
        elif choice == '3':
            index = int(input("Enter contact index: "))
            contact_book.delete_contact(index)
        elif choice == '4':
            name = input("Enter name to search: ")
            contact = contact_book.search_contact(name)
            if contact:
                print(f"Phone: {contact.phone}, Email: {contact.email}")
            else:
                print("Contact not found")
        elif choice == '5':
            break

if __name__ == "__main__":
    main()