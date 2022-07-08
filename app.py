import streamlit as st
import joblib
model = joblib.load('HeartDiseasePrediction')
st.title("""
#Heart Disease Prediction App
This App Predicts The Chances of a **Heart Disease** based on a Person's Medical Report
"""
)
op =[None]*13
ip = st.text_input(int('Enter the Age'))
op[0] = ip
ip2 = st.text_input(int('Enter the sex'))
op[1] = ip2
ip3 = st.text_input(int('Enter the chest pain type'))
op[2] = ip3
ip4 = st.text_input(int('Enter The resting blood pressure'))
op[3] = ip4
ip5 = st.text_input(int('Enter the cholestrol level'))
op[4] = ip5
ip6 = st.text_input(int('Enter the fasting blood sugar'))
op[5] = ip6
ip7 = st.text_input(int('Enter the resting electrocardiographic results'))
op[6] = ip7
ip8 = st.text_input(int('Enter the Maximum heart rate'))
op[7] = ip8
ip9 = st.text_input(int('Enter the exercise induced angina'))
op[8] = ip9
ip10 = st.text_input(int('Enter the oldpeak'))
op[9] = ip10
ip11 = st.text_input(int('Enter the the slope of the peak exercise ST segment'))
op[10] = ip11
ip12 = st.text_input(int('Enter the number of major vessels'))
op[11] = ip12
ip13 = st.text_input(int('Enter the thal: 0 = normal; 1 = fixed defect; 2 = reversable defect'))
op[12] = ip13
OP = model.predict([op])
if st.button('Predict'):
  st.title(OP[0])

  
