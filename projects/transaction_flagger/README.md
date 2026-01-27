# Transaction Flagger (Fintech Mini Project)

Rule-based transaction validation and flagging example.

## Business rules

INVALID:
- non-numeric amount
- amount <= 0

FLAG:
- high amount (>= 5000)
- high-risk country (NG)

OK:
- all other cases

## Skills practiced
- Python core syntax
- loops and conditionals
- data validation
- rule-based decision logic

## Run

```bash
cd projects/transaction_flagger
python3 main.py
