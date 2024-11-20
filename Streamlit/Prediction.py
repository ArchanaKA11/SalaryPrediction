import pandas as pd
import streamlit as st
import pickle
from PIL import Image


def main():
    global w , e, m, o, r, rc
    st.title(":red[SALARY PREDICTION]")
    img = Image.open('OIP.jpeg')
    st.image(img, width=850)
    age = st.text_input("Age", "")
    workclass = st.radio("Select Work Class",
                         ["Others", "Federal-gov", "Local-gov", "Never-worked", "Private", "Self-emp-inc",
                          "Self-emp-not-inc", "State-gov"])
    if workclass == 'Federal-gov':
        w = 0
    elif workclass == 'Local-gov':
        w = 1
    elif workclass == 'Never-worked':
        w = 2
    elif workclass == 'Private':
        w = 3
    elif workclass == 'Self-emp-inc':
        w = 4
    elif workclass == 'Self-emp-not-inc':
        w = 5
    elif workclass == 'State-gov':
        w = 6
    elif workclass == 'Others':
        w = 7
    education = st.radio("Select Education",
                         ["10th", "11th", "12th", "1st-4th", "5th-6th", "7th-8th", "9th", "Assoc-acdm", "Assoc-voc",
                          "Bachelors", "Doctorate", "HS-grad", "Masters", "Preschool", "Prof-school", "Some-college"])
    if education == '10th':
        e = 0
    elif education == '11th':
        e = 1
    elif education == '12th':
        e = 2
    elif education == '1st-4th':
        e = 3
    elif education == '5th-6th':
        e = 4
    elif education == '7th-8th':
        e = 5
    elif education == '9th':
        e = 6
    elif education == 'Assoc-acdm':
        e = 7
    elif education == 'Assoc-voc':
        e = 8
    elif education == 'Bachelors':
        e = 9
    elif education == 'Doctorate':
        e = 10
    elif education == 'HS-grad':
        e = 11
    elif education == 'Masters':
        e = 12
    elif education == 'Preschool':
        e = 13
    elif education == 'Prof-school':
        e = 14
    elif education == 'Some-college':
        e = 15
    # education_num = st.text_input("Education Number", "Pre school: 1\n,1st-4th: 2\n,5th-6th: 3\n,7th-8th: 4\n,9th: 5\n,10th: 6\n,11th: 7\n,12th: 8\n,HS-grad: 9\n,Some College: 10\n,Assoc-voc: 11\n,Assoc-acdm: 12\n,Bachelors: 13\n,Masters: 14\n,Prof-school: 15\n,Doctorate: 16")
    ###############################################3

    # Education level and corresponding education numbers
    # education_mapping = {
    #     "Pre school": 1,
    #     "1st-4th": 2,
    #     "5th-6th": 3,
    #     "7th-8th": 4,
    #     "9th": 5,
    #     "10th": 6,
    #     "11th": 7,
    #     "12th": 8,
    #     "HS-grad": 9,
    #     "Some College": 10,
    #     "Assoc-voc": 11,
    #     "Assoc-acdm": 12,
    #     "Bachelors": 13,
    #     "Masters": 14,
    #     "Prof-school": 15,
    #     "Doctorate": 16,
    # }
    #
    # # User input for education number
    # education_num = st.text_input("Enter Education Number:")
    #
    # # Display suggestions based on input
    # if education_num:
    #     try:
    #         num = int(education_num)
    #         for education, number in education_mapping.items():
    #             if number == num:
    #                 st.write(f"**Suggestion:** This number corresponds to **{education}**.")
    #                 break
    #         else:
    #             st.write("**Note:** Please enter a valid education number between 1 and 16.")
    #     except ValueError:
    #         st.write("**Error:** Please enter a numeric value for the education number.")

    # Instructions for education number

    education_num=st.text_input("Enter Education Number:")

    # Guidance on education numbers
    st.write("""
    **Guide for Education Number:**
    - Pre school: 1
    - 1st-4th: 2
    - 5th-6th: 3
    - 7th-8th: 4
    - 9th: 5
    - 10th: 6
    - 11th: 7
    - 12th: 8
    - HS-grad: 9
    - Some College: 10
    - Assoc-voc: 11
    - Assoc-acdm: 12
    - Bachelors: 13
    - Masters: 14
    - Prof-school: 15
    - Doctorate: 16
    """)

    marital_status = st.radio("Select Marital Status",
                              ["Divorced", "Married-AF-spouse", "Married-civ-spouse", "Married-spouse-absent",
                               "Never-married", "Separated", "Widowed"])
    if marital_status == 'Divorced':
        m = 0
    elif marital_status == 'Married-AF-spouse':
        m = 1
    elif marital_status == 'Married-civ-spouse':
        m = 2
    elif marital_status == 'Married-spouse-absent':
        m = 3
    elif marital_status == 'Never-married':
        m = 4
    elif marital_status == 'Separated':
        m = 5
    elif marital_status == 'Widowed':
        m = 6
    occupation = st.radio("Select Occupation",
                          ["Others", "Adm-clerical", "Armed-Forces", "Craft-repair", "Exec-managerial",
                           "Farming-fishing", "Handlers-cleaners", "Machine-op-inspct", "Other-service",
                           "Priv-house-serv", "Prof-specialty", "Protective-serv", "Sales", "Tech-support",
                           "Transport-moving"])
    if occupation == 'Adm-clerical':
        o = 0
    elif occupation == 'Armed-Forces':
        o = 1
    elif occupation == 'Craft-repair':
        o = 2
    elif occupation == 'Exec-managerial':
        o = 3
    elif occupation == 'Farming-fishing':
        o = 4
    elif occupation == 'Handlers-cleaners':
        o = 5
    elif occupation == 'Machine-op-inspct':
        o = 6
    elif occupation == 'Other-service':
        o = 7
    elif occupation == 'Priv-house-serv	':
        o = 8
    elif occupation == 'Prof-specialty':
        o = 9
    elif occupation == 'Protective-serv':
        o = 10
    elif occupation == 'Sales':
        o = 11
    elif occupation == 'Tech-support':
        o = 12
    elif occupation == 'Transport-moving':
        o = 13
    elif occupation == 'Others':
        o = 14
    relationship = st.radio("Select Relationship",
                            ["Husband", "Not-in-family", "Other-relative", "Own-child", "Unmarried", "Wife"])
    if relationship == 'Husband':
        r = 0
    elif relationship == 'Not-in-family':
        r = 1
    elif relationship == 'Other-relative':
        r = 2
    elif relationship == 'Own-child':
        r = 3
    elif relationship == 'Unmarried':
        r = 4
    elif relationship == 'Wife':
        r = 5
    race = st.radio("Select Race", ["Amer-Indian-Eskimo", "Asian-Pac-Islander", "Black", "Other", "White"])
    if race == 'Amer-Indian-Eskimo':
        rc = 0
    elif race == 'Asian-Pac-Islander':
        rc = 1
    elif race == 'Black':
        rc = 2
    elif race == 'Other':
        rc = 3
    elif race == 'White':
        rc = 4
    sex = st.radio("Select gender", ["Male", "Female"])
    if sex == 'Male':
        g = 1
    else:
        g = 0
    capital_gain = st.text_input("Capital Gain", "")
    capital_loss = st.text_input("Capital Loss", "")
    hours_per_week = st.text_input("Hours Per Week", "")
    features = [age, w, e, education_num, m, o, r, rc, g, capital_gain, capital_loss, hours_per_week]
    scaler2 = pickle.load(open('scalersalary.sav', 'rb'))
    model2 = pickle.load(open('modelsalary1.sav', 'rb'))
    features = pd.to_numeric(features, errors='coerce')
    pred = st.button("PREDICT")
    if pred:
        result = model2.predict(scaler2.transform([features]))
        if result == 0:
              st.write("Salary is <=50K")
        else:
              st.write("Salary is >50K")
main()




