import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('diabetes_model.sav', 'rb'))

def diabetes_prediction(input_data):
    data = np.asarray(input_data)
    data = data.reshape(1,-1)
    prediction = model.predict(data)
    if prediction:
        return 'Diabetes Positive'
    else:
        return 'Diabetes Negative'

def main():
    st.title('Diabetes Prediction Web App')

    # Getting data from user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age')
    
    diagnosis=''
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()