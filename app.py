import numpy as np
import pickle
import pandas as pd
import streamlit as st
lr = pickle.load(open("student_mark_predictor.pkl",'rb'))
def welcome():
    return "Welcome All"
def student_mark_predictor(study_hours):
    input = np.array([study_hours]).astype(np.float64).reshape(1,-1)

    prediction = lr.predict(input)
    return prediction[0].round(0)
def main():
    st.title("Nepal New Corona Case Predictor")
    html_temp="""
    <div style="background-color:orange;padding:10px">
    <h2 style="color:white'text-align:center;">Streamlit Nepal New Case Predictor ML App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    study_hours = st.text_input("Study_hours","Type Here")
   
    result=""
    if st.button("Predict"):
        result = student_mark_predictor(study_hours)
    st.success(f'The percentage that student will get is:{result}%')
    if st.button("About"):
        st.text("Nepal_Corona_New_Case_Predictor")
        st.text("Project for Machine Learning")
        st.text("© SantoshThapa 2020")
    
if __name__=='__main__':
    main()