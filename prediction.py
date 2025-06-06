import pandas as pd
import joblib

model = joblib.load('attrition_model.pkl')

sample = {
    'Age': 35,
    'BusinessTravel': 'Travel_Rarely',
    'DailyRate': 1100,
    'Department': 'Sales',
    'DistanceFromHome': 10,
    'Education': 3,
    'EducationField': 'Marketing',
    'EnvironmentSatisfaction': 3,
    'Gender': 'Male',
    'HourlyRate': 80,
    'JobInvolvement': 3,
    'JobLevel': 2,
    'JobRole': 'Sales Executive',
    'JobSatisfaction': 3,
    'MaritalStatus': 'Single',
    'MonthlyIncome': 7000,
    'MonthlyRate': 20000,
    'NumCompaniesWorked': 1,
    'Over18': 'Y',
    'OverTime': 'No',
    'PercentSalaryHike': 12,
    'PerformanceRating': 3,
    'RelationshipSatisfaction': 3,
    'StandardHours': 80,
    'StockOptionLevel': 1,
    'TotalWorkingYears': 10,
    'TrainingTimesLastYear': 3,
    'WorkLifeBalance': 2,
    'YearsAtCompany': 5,
    'YearsInCurrentRole': 3,
    'YearsSinceLastPromotion': 1,
    'YearsWithCurrManager': 3
}

sample_df = pd.DataFrame([sample])
prob = model.predict_proba(sample_df)[0][1]
print(f"Predicted attrition probability: {prob:.2%}")