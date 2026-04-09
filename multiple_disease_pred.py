# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:07:06 2026

@author: Chaitanya Kunjar
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from chatbot import get_chatbot_response

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "initialized" not in st.session_state:
    st.session_state.initialized = False

if "last_selected" not in st.session_state:
    st.session_state.last_selected = ""

# Loading the saved models

diabetes_model = pickle.load(
    open(
        "diabetes_model.sav",
        "rb",
    )
)

heart_disease_model = pickle.load(
    open(
        "heart_disease_model.sav",
        "rb",
    )
)

parkinsons_model = pickle.load(
    open(
        "parkinsons_model.sav",
        "rb",
    )
)

# Sidebar for navigation

with st.sidebar:
    selected = option_menu(
        "AI-Driven Multiple Disease Prediction",
        [
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Parkinsons Disease Prediction",
        ],
        icons=["activity", "heart", "person"],
        default_index=0,
    )
    
if st.session_state.last_selected != selected:
    st.session_state.chat_history = []
    st.session_state.initialized = False
    st.session_state.last_selected = selected

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    # Page title
    st.title("Diabetes Prediction using ML")

    # Columns for input fields
    col1, col2, col3 = st.columns(3)

    # Getting the input data from user
    with col1:
        Pregnancies = st.text_input("Number of pregnancies")
    with col2:
        Glucose = st.text_input("Glucose level")
    with col3:
        BloodPressure = st.text_input("Blood pressure value")
    with col1:
        SkinThickness = st.text_input("Skin thickness value")
    with col2:
        Insulin = st.text_input("Insulin level")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes pedigree function value")
    with col2:
        Age = st.text_input("Age of the person")

    # Code for prediction
    diab_diagnosis = ""

    # Creating a button for prediction
    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict(
            [
                [
                    float(Pregnancies),
                    float(Glucose),
                    float(BloodPressure),
                    float(SkinThickness),
                    float(Insulin),
                    float(BMI),
                    float(DiabetesPedigreeFunction),
                    float(Age),
                ]
            ]
        )
        # Print the result
        if diab_prediction[0] == 1:
            diab_diagnosis = "High Risk of Diabetes"
        else:
            diab_diagnosis = "Low Risk of Diabetes"
            
        prediction_summary = f"""
        Disease: Diabetes
        Risk: {diab_diagnosis}
        Glucose: {Glucose}
        BMI: {BMI}
        Age: {Age}
        """

    st.success(diab_diagnosis)
    
    if diab_diagnosis != "":

        st.subheader("🤖 AI Health Assistant")

        # Auto AI explanation
        if not st.session_state.initialized:
            intro = get_chatbot_response(
                "Explain my diabetes condition and what I should do",
                prediction_summary,
                []
            )
            st.session_state.chat_history.append(("assistant", intro))
            st.session_state.initialized = True
    
        # user_input = st.text_input("Ask about your condition...")
    
        # if user_input:
        #     response = get_chatbot_response(
        #         user_input,
        #         prediction_summary,
        #         st.session_state.chat_history
        #     )
    
        #     st.session_state.chat_history.append(("user", user_input))
        #     st.session_state.chat_history.append(("assistant", response))
    
        # Display chat
        for role, message in st.session_state.chat_history:
            if role == "user":
                st.write(f"🧑 You: {message}")
            else:
                st.write(f"🤖 AI: {message}")

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    # Page title
    st.title("Heart Disease Prediction using ML")

    # Columns for input fields
    col1, col2, col3 = st.columns(3)

    # Getting the input data from user
    with col1:
        age = st.text_input("Age")
    with col2:
        sex = st.text_input("Sex")
    with col3:
        cp = st.text_input("Chest Pain types")
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
    with col2:
        chol = st.text_input("Serum Cholestoral in mg/dl")
    with col3:
        fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl")
    with col1:
        restecg = st.text_input("Resting Electrocardiographic results")
    with col2:
        thalach = st.text_input("Maximum Heart Rate achieved")
    with col3:
        exang = st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak = st.text_input("ST depression induced by exercise")
    with col2:
        slope = st.text_input("Slope of the peak exercise ST segment")
    with col3:
        ca = st.text_input("Major vessels colored by flourosopy")
    with col1:
        thal = st.text_input(
            "thal: 0 = normal; 1 = fixed defect; 2 = reversable defect"
        )

    # Code for Prediction
    heart_diagnosis = ""

    # Creating a button for Prediction
    if st.button("Heart Disease Test Result"):
        user_input = [
            age,
            sex,
            cp,
            trestbps,
            chol,
            fbs,
            restecg,
            thalach,
            exang,
            oldpeak,
            slope,
            ca,
            thal,
        ]
        user_input = [float(x) for x in user_input]
        # Make prediction
        heart_prediction = heart_disease_model.predict([user_input])
        # Print the result
        if heart_prediction[0] == 1:
            heart_diagnosis = "The person is having heart disease"
        else:
            heart_diagnosis = "The person does not have any heart disease"

    st.success(heart_diagnosis)
    
    if heart_diagnosis != "":

        prediction_summary = f"""
        Disease: Heart Disease
        Result: {heart_diagnosis}
        Age: {age}
        Cholesterol: {chol}
        Blood Pressure: {trestbps}
        """
    
        st.subheader("🤖 AI Health Assistant")
    
        if not st.session_state.initialized:
            intro = get_chatbot_response(
                "Explain my heart condition and what I should do",
                prediction_summary,
                []
            )
            st.session_state.chat_history.append(("assistant", intro))
            st.session_state.initialized = True
    
        # user_input = st.text_input("Ask about your heart health...")
    
        # if user_input:
        #     response = get_chatbot_response(
        #         user_input,
        #         prediction_summary,
        #         st.session_state.chat_history
        #     )
    
        #     st.session_state.chat_history.append(("user", user_input))
        #     st.session_state.chat_history.append(("assistant", response))
    
        for role, message in st.session_state.chat_history:
            if role == "user":
                st.write(f"🧑 You: {message}")
            else:
                st.write(f"🤖 AI: {message}")

# Parkinsons Disease Prediction Page
if selected == "Parkinsons Disease Prediction":
    # Page title
    st.title("Parkinsons Disease Prediction using ML")

    # Columns for input fields
    col1, col2, col3, col4, col5 = st.columns(5)

    # Getting the input data from user
    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")
    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col1:
        RAP = st.text_input("MDVP:RAP")
    with col2:
        PPQ = st.text_input("MDVP:PPQ")
    with col3:
        DDP = st.text_input("Jitter:DDP")
    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")
    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")
    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")
    with col3:
        APQ = st.text_input("MDVP:APQ")
    with col4:
        DDA = st.text_input("Shimmer:DDA")
    with col5:
        NHR = st.text_input("NHR")
    with col1:
        HNR = st.text_input("HNR")
    with col2:
        RPDE = st.text_input("RPDE")
    with col3:
        DFA = st.text_input("DFA")
    with col4:
        spread1 = st.text_input("spread1")
    with col5:
        spread2 = st.text_input("spread2")
    with col1:
        D2 = st.text_input("D2")
    with col2:
        PPE = st.text_input("PPE")

    # Code for Prediction
    parkinsons_diagnosis = ""

    # Creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        user_input = [
            fo,
            fhi,
            flo,
            Jitter_percent,
            Jitter_Abs,
            RAP,
            PPQ,
            DDP,
            Shimmer,
            Shimmer_dB,
            APQ3,
            APQ5,
            APQ,
            DDA,
            NHR,
            HNR,
            RPDE,
            DFA,
            spread1,
            spread2,
            D2,
            PPE,
        ]
        user_input = [float(x) for x in user_input]
        # Making prediction
        parkinsons_prediction = parkinsons_model.predict([user_input])
        # Print the result
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    if parkinsons_diagnosis != "":

        prediction_summary = f"""
        Disease: Parkinson's
        Result: {parkinsons_diagnosis}
        Fo: {fo}
        Jitter: {Jitter_percent}
        Shimmer: {Shimmer}
        """
    
        st.subheader("🤖 AI Health Assistant")
    
        if not st.session_state.initialized:
            intro = get_chatbot_response(
                "Explain Parkinson's condition and next steps",
                prediction_summary,
                []
            )
            st.session_state.chat_history.append(("assistant", intro))
            st.session_state.initialized = True
    
        # user_input = st.text_input("Ask about Parkinson's...")
    
        # if user_input:
        #     response = get_chatbot_response(
        #         user_input,
        #         prediction_summary,
        #         st.session_state.chat_history
        #     )
    
        #     st.session_state.chat_history.append(("user", user_input))
        #     st.session_state.chat_history.append(("assistant", response))
    
        for role, message in st.session_state.chat_history:
            if role == "user":
                st.write(f"🧑 You: {message}")
            else:
                st.write(f"🤖 AI: {message}")
