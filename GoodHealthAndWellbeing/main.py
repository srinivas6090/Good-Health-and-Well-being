def generate_recommendations(patient_data):
    recommendations = []
    if patient_data['BMI'] > 25:
        recommendations.append("Consider a balanced diet to manage weight.")
    if patient_data['PhysicalActivity'] < 2:
        recommendations.append("Increase weekly physical activity.")
    return recommendations

# Sample patient data
patient_data = {'BMI': 28, 'PhysicalActivity': 1}
print(generate_recommendations(patient_data))
