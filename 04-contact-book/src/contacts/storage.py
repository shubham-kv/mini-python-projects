import json
from pathlib import Path

contacts_data_path = Path.home() / ".contacts.json"


def load_contacts() -> list[dict[str, int | str | None]]:
    if contacts_data_path.exists():
        try:
            with open(contacts_data_path, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []


def save_contacts(contacts: list[dict[str, int | str | None]]):
    with open(contacts_data_path, "w") as file:
        json.dump(contacts, file, indent=2)
