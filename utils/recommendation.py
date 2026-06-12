def get_treatment_recommendation(
    disease
):

    recommendations = {

        "Diabetes": {
            "specialist": "Endocrinologist",
            "tests": [
                "HbA1c Test",
                "Blood Glucose Test"
            ],
            "advice": [
                "Reduce sugar intake",
                "Exercise daily"
            ]
        },

        "Heart Disease": {
            "specialist": "Cardiologist",
            "tests": [
                "ECG",
                "Echocardiogram"
            ],
            "advice": [
                "Low-fat diet",
                "Regular exercise"
            ]
        },

        "Kidney Disease": {
            "specialist": "Nephrologist",
            "tests": [
                "Creatinine Test",
                "Urine Analysis"
            ],
            "advice": [
                "Drink adequate water",
                "Limit salt intake"
            ]
        },

        "Asthma": {
            "specialist": "Pulmonologist",
            "tests": [
                "Spirometry",
                "Chest X-Ray"
            ],
            "advice": [
                "Avoid dust",
                "Use inhaler as prescribed"
            ]
        },

        "Healthy": {
            "specialist": "None",
            "tests": [
                "Annual Checkup"
            ],
            "advice": [
                "Maintain healthy lifestyle"
            ]
        }
    }

    return recommendations.get(
        disease,
        {
            "specialist": "General Physician",
            "tests": [],
            "advice": [
                "Consult a healthcare professional"
            ]
        }
    )