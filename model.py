import pickle

model = pickle.load(open('model.pkl','rb'))

def check_loan(income, credit, loan, age):
    input_data = [[income, credit, loan, age]]

    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    reasons = []
    suggestions = []
    score = 0

    # AGE
    if age < 21:
        reasons.append("Applicant is below minimum eligible age (21).")
        suggestions.append("Apply after reaching 21 years.")
        score -= 2
    elif age > 60:
        reasons.append("Applicant age is above preferred limit (60).")
        suggestions.append("Provide additional documents.")
        score -= 1
    else:
        score += 1

    # CREDIT
    if credit >= 750:
        score += 2
    elif credit >= 650:
        score += 1
    else:
        reasons.append("Poor credit score.")
        suggestions.append("Improve credit score above 700.")
        score -= 2

    # INCOME
    if income >= 50000:
        score += 2
    elif income >= 25000:
        score += 1
    else:
        reasons.append("Low income.")
        suggestions.append("Increase income.")
        score -= 2

    # LOAN
    if loan <= income * 5:
        score += 2
    elif loan <= income * 8:
        score += 1
    elif loan <= income * 10:
        score -= 1
    else:
        reasons.append("Loan too high compared to income.")
        suggestions.append("Apply for smaller loan.")
        score -= 2

    # FINAL DECISION
    final_status = "Approved" if (score >= 3 and prediction == 1) else "Rejected"

    if final_status == "Approved":
        final_prob = prob * 100
    else:
        final_prob = (1 - prob) * 100

    if final_status == "Approved":
        return {
            "status": "Approved",
            "statement": f"Congratulations! Your loan is approved with {round(final_prob,2)}% confidence.",
            "reasons": ["Strong financial profile", "Good repayment capacity"],
            "suggestions": ["Maintain financial discipline."]
        }
    else:
        return {
            "status": "Rejected",
            "statement": f"Unfortunately, your loan is rejected with {round(final_prob,2)}% confidence.",
            "reasons": reasons if reasons else ["Multiple risk factors detected."],
            "suggestions": suggestions if suggestions else ["Improve financial profile."]
        }