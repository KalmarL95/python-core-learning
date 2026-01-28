import csv
from rules import RULES


def parse_amount(text):
    try:
        return float(text)
    except ValueError:
        return None


def validate_transaction(amount_text, currency, country):
    amount = parse_amount(amount_text)

    if amount is None:
        return "invalid", "parse_error"

    if amount <= 0:
        return "invalid", "non_positive_number"

    if currency not in RULES["currency"]["allowed"]:
        return "flag", RULES["currency"]["reason"]

    if country in RULES["high_risk_countries"]["countries"]:
        return "flag", RULES["high_risk_countries"]["reason"]

    for rule in RULES["amount_rules"]:
        if amount >= rule["min"]:
            return rule["status"], rule["reason"]

    return "ok", "normal"


def main():
    results = []

    with open("transactions.csv", newline="") as infile:
        reader = csv.DictReader(infile)

        for row in reader:
            status, reason = validate_transaction(
                row["amount"],
                row["currency"],
                row["country"]
            )

            results.append({
                "tx_id": row["tx_id"],
                "amount": row["amount"],
                "currency": row["currency"],
                "country": row["country"],
                "status": status,
                "reason": reason
            })

    with open("results.csv", "w", newline="") as outfile:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)


if __name__ == "__main__":
    main()

