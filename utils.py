import phonenumbers
from phonenumbers import NumberParseException

def parse_and_format_phone_number(phone_number):
    """Parse and format the phone number, returning E.164 format or None if invalid."""
    try:
        parsed_number = phonenumbers.parse(phone_number, "US")
        return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
    except NumberParseException:
        return None

def sanitize_phone_number(phone_number):
    """Sanitize and validate the phone number."""
    formatted_number = parse_and_format_phone_number(phone_number)
    return formatted_number if phonenumbers.is_valid_number(phonenumbers.parse(formatted_number, "US")) else None

def sanitize_no_validation(phone_number):
    """Sanitize the phone number without validation."""
    return parse_and_format_phone_number(phone_number)
