import streamlit as st
import pickle
import pandas as pd
import numpy as np
from PIL import Image

file = pickle.load(open("C:\\Users\\Rotimi\\Downloads\\ln_regproject.pkl", 'rb'))

st.title('Welcome to Spent Calories Predictor')
st.text("This app allows users who have just completed exercise sessions estimate how \nmuch calories they used up during the exercise session.")
st.sidebar.header('User\'s Data')
user_image = Image.open("C:\\Users\\Rotimi\\Downloads\\calories_img.jpg")
st.image(user_image, width=500)
# creating a function for the values

def report():
    Gender = st.sidebar.selectbox('Select Gender', ['Male', 'Female'])
    if Gender == 'Female':
        Gender = 0,
    else:
        Gender = 1
    Age = st.sidebar.slider('Enter Age', 1,100)
    h_status = st.sidebar.radio('Select your height format: ', ('cms', 'meters', 'feet'))
    if (h_status == 'cms'):
        Height = st.sidebar.number_input('Centimeters'),
    elif (h_status == 'meters'):
        Height = st.sidebar.number_input('meters')
        try:
            Height = Height * 100
        except:
            st.text("Enter the value of height"),
    else:
        Height = st.sidebar.number_input('feet')
        try:
            Height = Height * 30.48
        except:
            st.text("Enter the value of height")
    w_status = st.sidebar.radio('Select your weight format: ', ('kgs', 'Ibs'))
    if (w_status == 'kgs'):
        Weight = st.sidebar.number_input('kgs'),
    else:
        Weight = st.sidebar.number_input('Ibs')
        try:
            Weight = (Weight / 2.2)
        except:
            st.text('Enter the value of weight')
    Duration = st.sidebar.number_input('Enter time spent exercising in minutes')
    Heart_rate = st.sidebar.number_input('Enter heart rate recorded during exercise')
    body_temp_format = st.sidebar.radio('Select temperature format', ('Celcius', 'Farenheit'))
    if (body_temp_format == 'Celcius'):
        Body_Temp = st.sidebar.number_input('Celcius'),
    else:
        Body_Temp = st.sidebar.number_input('Farenheit')
        try:
            Body_Temp = (Body_Temp - 32) * (5 / 9)
        except:
            st.text('Enter the value for body temperature')
    # creating a dictionary of the values
    report_data = {
        'Gender': Gender,
        'Age': Age,
        'Height': Height,
        'Weight': Weight,
        'Duration': Duration,
        'Heart_Rate': Heart_rate,
        'Body_Temp': Body_Temp}
    report_data = pd.DataFrame(report_data, index=[0])
    return report_data

user_data = report()

st.subheader('User\'s summary')
st.write(user_data)

calories_spent = file.predict(user_data)
if (st.sidebar.button('Calculate Calories Spent')):
    st.subheader(f"Total calories spent while exercising is {np.round(calories_spent)} kcal. ")