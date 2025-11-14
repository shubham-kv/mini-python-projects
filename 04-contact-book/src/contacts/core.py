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
