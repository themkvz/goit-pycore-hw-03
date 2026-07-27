import re


def normalize_phone(phone_number: str) -> str:
    input_phone = phone_number.strip()

    if not input_phone:
        return ""

    input_phone = re.sub(r"[^\d]", "", input_phone)

    if input_phone.startswith("380"):
        input_phone = "+" + input_phone
    elif input_phone.startswith("0"):
        input_phone = "+38" + input_phone

    if re.match(r"^\+380\d{9}$", input_phone):
        return input_phone

    return ""

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print(sanitized_numbers)

assert normalize_phone("") == ""
assert normalize_phone("   ") == ""
assert normalize_phone("1234567890") == ""
assert normalize_phone("38050123456") == ""
assert normalize_phone("380501234567") == "+380501234567"
