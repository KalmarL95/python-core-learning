def parse_amount(text):
    try:
        return float(text)
    except ValueError:
        return None


def validate_transaction(amount_text, currency):
    amount = parse_amount(amount_text)

    if amount is None:
        return "invalid", "parse_error"

    if amount <= 0:
        return "invalid", "non_positive_amount"

    if currency != "EUR":
        return "flag", "foreign_currency"

    if amount >= 5000:
        return "flag", "high_amount"

    return "ok", "normal"


transactions = [
    ("120.5", "EUR"),
    ("-50", "EUR"),
    ("10000", "EUR"),
    ("abc", "EUR"),
    ("2500", "USD"),
]

for amount, currency in transactions:
    status, reason = validate_transaction(amount, currency)
    print(amount, currency, "=>", status, reason)


