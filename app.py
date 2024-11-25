import streamlit as st
import pandas as pd
import joblib
model=joblib.load("Linear Regression")
def predection(cgpa):
    cgpa=float(cgpa)
    prediction_placement=model.predict([[cgpa]])
    return prediction_placement
def main():
    st.title("Placement Prediction")
    st.sidebar.title("User input")
    age=st.sidebar.slider("Age",18,25,18)
    name=st.sidebar.text_input("Enter your name: ")
    sex=st.sidebar.radio("Enter your gender: ",["Male","Female","Other"])
    Phone_no=st.sidebar.number_input("Enter your phone number: ",step=1)
    degree = st.sidebar.selectbox("Choose your degree", ["B.tech", "Bsc", "Other"])  
    cgpa=st.sidebar.text_input("Enter your sugested cgpa: ",0,10)
    st.subheader("Confirmation")
    st.write("Age=",age)
    st.write("Your Name :",name)
    st.write("Phone_number :",Phone_no)
    st.write("Degree :",degree)
    st.write("cgpa:",cgpa)
    st.write("Sex:",sex)
    if st.button('click me!'):
        prediction_=predection(cgpa)
        st.write(f"Sugested pakage for {name} with persuing {degree}, is likey to get --> {prediction_} crPA,congratulations")
main()
