'''score = 72

if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")


name = "Levente"

if name.lower().startswith("lev"):
    print("Name starts with 'lev'")
else:
    print("Different name")


weight_text = "71.5"
height_text = "182"

# 1) Parse/validate
try:
    weight = float(weight_text)
    height = float(height_text)
except ValueError:
    print("INVALID: weight or height is not a number")
    weight = None
    height = None

if weight is not None and height is not None:
    print("VALID numbers:", weight, height)

# 2) Business validation
if weight is None or height is None:
    status = "INVALID"
    reason = "parse_error"
elif weight <= 0 or height <= 0:
    status = "INVALID"
    reason = "non_positive_values"
else:
    # 3) Compute
    bmi = weight / ((height / 100) ** 2)

    # 4) Flag rules
    if bmi < 18.5:
        status = "FLAG"
        reason = "underweight"
    elif bmi < 25:
        status = "OK"
        reason = "normal weight"
    elif bmi < 30:
        status = "FLAG"
        reason = "overweight"
    else:
        status = "FLAG"
        reason = "obese"

    print("BMI:", round(bmi, 2))

print("STATUS:", status)
print("REASON:", reason)'''

people = [
    {"name": "Levente", "weight": "71.5", "height": "182"},
    {"name": "Anna", "weight": "48", "height": "165"},
    {"name": "Bela", "weight": "0", "height": "175"},
    {"name": "Chris", "weight": "abc", "height": "180"},
]

'''for person in people:
    name = person["name"]
    weight_text = person["weight"]
    height_text = person["height"]

    try:
        weight = float(weight_text)
        height = float(height_text)
    except ValueError:
        status = "INVALID"
        reason = "parse_error"
        print(name, status, reason)
        continue

    if weight <= 0 or height <= 0:
        status = "INVALID"
        reason = "non_positive_values"
    else:
        bmi = weight / ((height / 100) ** 2)

        if bmi < 18.5:
            status = "FLAG"
            reason = "underweight"
        elif bmi < 25:
            status = "OK"
            reason = "normal weight"
        elif bmi < 30:
            status = "FLAG"
            reason = "overweight"
        else:
            status = "FLAG"
            reason = "obese"

        print(name, "BMI:", round(bmi, 2))

    print(name, "STATUS:", status, "REASON:", reason)
    print("-" * 30)'''

def parse_float(text):
    """Try to convert text to float. Return float or None if invalid."""
    try:
        return float(text)
    except ValueError:
        return None

def evaluate_person(person):
    """
    Returns a result dict with:
    - name
    - status: OK / FLAG / INVALID
    - reason
    - bmi (optional)
    """
    name = person["name"]

    weight = parse_float(person["weight"])
    height = parse_float(person["height"])

    if weight is None or height is None:
        return {"name": name, "status": "Invalid", "reason": "parse_error"}
    if weight <=0 or height <=0:
        return {"name": name, "status": "invalid", "reason": "non_positive_values"}

    bmi = weight / ((height / 100) ** 2)

    if bmi < 18.5:
        return {"name": name, "status": "FLAG", "reason": "underweight", "bmi": round(bmi, 2)}
    elif bmi < 25:
        return {"name": name, "status": "OK", "reason": "normal weight", "bmi": round(bmi, 2)}
    elif bmi < 30:
        return {"name": name, "status": "FLAG", "reason": "overweight", "bmi": round(bmi, 2)}
    else:
        return {"name": name, "status": "FLAG", "reason": "obese", "bmi": round(bmi, 2)}

def main():
    results = []

    for person in people:
        result = evaluate_person(person)
        results.append(result)

    for r in results:
        if "bmi" in r:
            print(f'{r["name"]} | BMI:{r["bmi"]} | {r["status"]} | {r["reason"]}')
        else:
            print(f'{r["name"]} | {r["status"]} | {r["reason"]}')

if __name__ == "__main__":
    main()













