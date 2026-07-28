import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return []

    result = set()

    while len(result) < quantity:
        number = random.randint(min, max)

        if (number in result):
            continue

        result.add(number)

    return sorted(result)

print(get_numbers_ticket(1, 100, 5))
print(get_numbers_ticket(10, 20, 5))

assert get_numbers_ticket(0, 100, 5) == []
assert get_numbers_ticket(1, 100, 0) == []
assert get_numbers_ticket(1, 100, 101) == []
assert get_numbers_ticket(1, 10001, 1) == []
