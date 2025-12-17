class Contact:
    def __init__(self, name, phone_number ):
        self.name = name
        self.phone_number = phone_number

    def  validate_phone_number(phone_number):
        if len(phone_number) == 10:
            return True
        else:
            return False



class ContactList:
    all_contacts = []

    def add_contact(name, phone_number):
        Contact.validate_phone_number(phone_number)


ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    if Contact.validate_phone_number(contact.phone_number):
        ContactList.add_contact("Вася Пупкин", "0700100200")
        print(contact.name, contact.phone)
    elif ContactList.add_contact("John Doe", "5551234"):
        print("Ошибка")

print(ContactList.all_contacts)
