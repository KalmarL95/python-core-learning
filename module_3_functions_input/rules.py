RULES = {
    "currency": {
        "allowed": ["EUR"],
        "reason": "foreign_currency"
    },
    "high_risk_countries": {
        "countries": ["NG"],
        "reason": "high_risk_country"
    },
    "amount_rules": [
        {"min": 10000, "status": "flag", "reason": "very_high_amount"},
        {"min": 5000, "status": "flag", "reason": "high_amount"}
    ]
}
