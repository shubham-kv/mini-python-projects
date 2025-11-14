from datetime import datetime

from contacts.storage import load_contacts, save_contacts
from contacts.utils import parse_email, parse_phone


def add_contact(
    name: str, phone: str | None, email: str | None
) -> None | dict[str, int | str | None]:
    if phone:
        err, formatted_phone = parse_phone(phone)

        if err:
            print("Invalid Phone, " + err)
            return None

        phone = formatted_phone

    if email:
        err, normalized_email = parse_email(email)

        if err:
            print("Invalid Email, " + err)
            return None

        email = normalized_email

    contacts = load_contacts()

    new_contact = {
        "id": len(contacts),
        "name": name,
        "phone": phone,
        "email": email,
        "created_at": datetime.now().__str__(),
    }

    contacts.append(new_contact)
    save_contacts(contacts)

    return new_contact


def search_contacts(query: str):
    contacts = load_contacts()
    found = [c for c in contacts if query.lower() in str(c["name"]).lower()]
    return found


def print_contacts(contacts: list[dict[str, int | str | None]]):
    if len(contacts) == 0:
        return

    row_format = " %2s | %-20s | %-15s | %s "

    print(row_format % ("Id", "Name", "Phone", "Email"))

    for c in contacts:
        print(row_format % (c["id"], c["name"], c["phone"], c["email"]))


def delete_contact(id: int) -> bool:
    contacts = load_contacts()
    index = next((i for i, c in enumerate(contacts) if c["id"] == id), -1)

    if index <= -1:
        return False

    del contacts[index]
    save_contacts(contacts)
    return True
