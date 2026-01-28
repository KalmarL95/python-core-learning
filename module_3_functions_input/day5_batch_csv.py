import csv


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
        return "invalid", "non_positive_amount"

    if currency != "EUR":
        return "flag", "foreign_currency"

    if country == "NG":
        return "flag", "high_risk_country"

    if amount >= 10000:
        return "flag", "very_high_amount"

    if amount >= 5000:
        return "flag", "high_amount"

    return "ok", "normal"


def main():
    results =[]
    summary = {"ok": 0, "flag": 0, "invalid": 0, "very_high_amount": 0}

    with open("transactions.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            status, reason = validate_transaction(
                row["amount"],
                row["currency"],
                row["country"]
            )

            results.append({
                "tx_id": row["tx_id"],
                "status": status,
                "reason": reason
            })

            summary[status] += 1
            if reason == "very_high_amount":
                summary["very_high_amount"] += 1

    print("Transaction results:")
    for r in results:
        print(f'{r["tx_id"]}: {r["status"]} | {r["reason"]}')

    print("\nSummary:")
    for k, v in summary.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
