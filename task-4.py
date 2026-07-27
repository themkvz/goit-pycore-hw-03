from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Bob Brown", "birthday": "1988.07.29"}, # Wednesday
    {"name": "Charlie Davis", "birthday": "1992.08.01"}, # Saturday
    {"name": "Alice Johnson", "birthday": "1995.08.04"}, # Tuesday
]

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_str = user.get("birthday")

        if not birthday_str:
            continue

        birthday = datetime.strptime(birthday_str, "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if (birthday_this_year < today):
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if (birthday_this_year - today).days <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() in [5, 6]:
                congratulation_date += timedelta(days=7 - congratulation_date.weekday())

            upcoming_birthdays.append({"name": user.get("name"), "congratulation_date": congratulation_date.strftime("%Y.%m.%d")})

    return upcoming_birthdays

print(get_upcoming_birthdays(users))

assert get_upcoming_birthdays([]) == []
