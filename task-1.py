from datetime import datetime


def get_days_from_today(date_str: str) -> int:
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d")
    except (ValueError, TypeError):
        return 0

    today = datetime.today()
    delta = today - input_date

    return delta.days

print(get_days_from_today("2023-01-01"))

assert get_days_from_today("2000-01-01") == (datetime.now() - datetime(2000, 1, 1)).days
assert get_days_from_today("2099-01-01") == (datetime.now() - datetime(2099, 1, 1)).days
assert get_days_from_today("Incorrect date format") == 0
assert get_days_from_today("") == 0
