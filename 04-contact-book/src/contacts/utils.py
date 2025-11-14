import phonenumbers
from email_validator import EmailNotValidError, validate_email


def parse_phone(phone: str):
    try:
        phone_number = phonenumbers.parse(phone, None)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        return (e._msg, "")

    if not phonenumbers.is_possible_number(phone_number):
        return ("Number is not a possible number.", "")

    if not phonenumbers.is_valid_number(phone_number):
        return ("Number is not valid.", "")

    formatted_phone = phonenumbers.format_number(
        phone_number, phonenumbers.PhoneNumberFormat.NATIONAL
    )

    return (None, formatted_phone)


def parse_email(email: str):
    try:
        v = validate_email(email)
        return ("", v.normalized)
    except EmailNotValidError as e:
        return (str(e), None)
