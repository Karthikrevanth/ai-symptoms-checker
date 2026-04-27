from symptoms_data import disease_data

def get_disease(user_symptoms):
    scores = {}

    for disease, symptoms in disease_data.items():
        match_count = 0
        for symptom in user_symptoms:
            if symptom in symptoms:
                match_count += 1
        scores[disease] = match_count

    predicted = max(scores, key=scores.get)

    if scores[predicted] == 0:
        return "No matching disease found. Please consult a doctor.", 0

    confidence = scores[predicted] / len(user_symptoms)
    return predicted, confidence


print("🤖 AI Symptom Checker (Prototype)")
print("Type symptoms separated by comma (example: fever, cough)")

user_input = input("You: ")

# Clean input (important)
user_symptoms = [s.strip().lower() for s in user_input.split(",")]

result, confidence = get_disease(user_symptoms)

if confidence == 0:
    print("Bot:", result)
else:
    print(f"Bot: {result} (Confidence: {confidence:.2f})")