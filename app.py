import streamlit as st
import joblib
model = joblib.load('HeartDiseasePrediction')
st.title("""
#Heart Disease Prediction App
This App Predicts The Chances of a **Heart Disease** based on a Person's Medical Report
"""
)
op =[None]*13
ip = st.number_input('Enter the Age')
op[0] = ip
ip2 = st.number_input('Enter the sex')
op[1] = ip2
ip3 = st.number_input('Enter the chest pain type')
op[2] = ip3
ip4 = st.number_input('Enter The resting blood pressure')
op[3] = ip4
ip5 = st.number_input('Enter the cholestrol level')
op[4] = ip5
ip6 = st.number_input('Enter the fasting blood sugar')
op[5] = ip6
ip7 = st.number_input('Enter the resting electrocardiographic results')
op[6] = ip7
ip8 = st.number_input('Enter the Maximum heart rate')
op[7] = ip8
ip9 = st.number_input('Enter the exercise induced angina')
op[8] = ip9
ip10 = st.number_input('Enter the oldpeak')
op[9] = ip10
ip11 = st.number_input('Enter the the slope of the peak exercise ST segment')
op[10] = ip11
ip12 = st.number_input('Enter the number of major vessels')
op[11] = ip12
ip13 = st.number_input('Enter the thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
op[12] = ip13
OP = model.predict([op])
if st.button('Predict'):
  st.title(OP[0])

  
