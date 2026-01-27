from data import TRANSACTIONS

def parse_amount(text):
    try:
        return float(text)
    except ValueError:
        return None

def evaluate_transaction(tx):
    tx_id = tx.get("tx_id", "UNKNOWN")
    country = tx.get("country", "UNKNOWN")

    amount = parse_amount(tx.get("amount", ""))

    if amount is None:
        return {"tx_id": tx_id, "status": "invalid", "reason": "amount_parse_error"}

    if amount <= 0:
        return {"tx_id": tx_id, "status": "invalid", "reason": "non_positive_amount"}

    if amount >= 5000:
        return {"tx_id": tx_id, "status": "flag", "reason": "high_amount"}

    if country == "NG":
        return {"tx_id": tx_id, "status": "flag", "reason": "high_risk_country"}

    return {"tx_id": tx_id, "status": "ok", "reason": "normal"}


def summarize(results):
    summary = {"ok": 0, "flag": 0, "invalid": 0}
    for r in results:
        summary[r["status"]] += 1
    return summary


def main():
    results = []

    for tx in TRANSACTIONS:
        results.append(evaluate_transaction(tx))

    print("Transaction results:")
    for r in results:
        print (f'- {r["tx_id"]}: {r["status"]} | {r["reason"]}')

    s = summarize(results)
    print("\nSummary:")
    print(s)


if __name__ == "__main__":
    main()

