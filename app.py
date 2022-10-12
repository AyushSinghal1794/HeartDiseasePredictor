import streamlit as st
import pandas as pd
import pickle
import joblib

df = pd.read_csv("HeartDiseasePrediction.csv")
male_age = 0
males = 0
female_age=0
females = 0
for i in range(0,302,1):
  if df['sex'][i] == 0:
    male_age = male_age + df['age'][i]
    males = males + 1
  elif df['sex'][i] == 1:
    female_age = female_age + df['age'][i]
    females = females + 1

avg_male_age = round(male_age/males,2)
avg_female_age = round(female_age/females,2)

male_cp = 0
female_cp = 0
males = 0
females = 0
for i in range(0,302,1):
  if df['sex'][i] == 1:
    male_cp = male_cp + df['cp'][i]
    males = males+1
  else:
    female_cp = female_cp + df['cp'][i]
    females = females + 1

avg_male_cp = round(male_cp/males,2)
avg_female_cp = round(female_cp/females,2)

male_trestbps = 0
female_trestbps = 0
males = 0
females = 0

for i in range(0,302,1):
  if df['sex'][i] == 1:
    male_trestbps = male_trestbps + df['trestbps'][i]
    males = males+1
  else:
    female_trestbps = female_trestbps + df['trestbps'][i]
    females = females+1

avg_male_trbps = round(male_trestbps/males,2)
avg_female_trbps = round(female_trestbps/females,2)

male_chol = 0
female_chol = 0
males = 0
females = 0

for i in (0,302,1):
  if df['sex'][i] == 1:
    male_chol = male_chol + df['chol'][i]
    males = males + 1
  else:
    female_chol = female_chol + df['chol'][i]
    females = females + 1

avg_male_chol = round(male_chol/males,2)
avg_female_chol = round(female_chol/females,2)

male_fbs = 0
female_fbs = 0
males = 0
females = 0
for i in range(0,302,1):
  if df['sex'][i] == 1:
    male_fbs = male_fbs + df['fbs'][i]
    males = males + 1
  else:
    female_fbs = female_fbs + df['fbs'][i]
    females = females + 1 

avg_male_fbs = round(male_fbs/males,4)
avg_female_fbs = round(female_fbs/females,4)

male_ecg = 0
female_ecg = 0
males = 0
females = 0
for i in range(0,302,1):
  if df['sex'][i] == 1:
    male_ecg = male_ecg + df['restecg'][i]
    males =males+1
  else:
    female_ecg = female_ecg + df['restecg'][i]
    females = females+1
avg_male_ecg = round(male_ecg/males,4)
avg_female_ecg = round(female_ecg/females,4)

male_thalach = 0
female_thalach = 0
males = 0
females = 0

for i in range(0,302,1):
  if df['sex'][i] == 1:
    male_thalach = male_thalach + df['thalach'][i]
    males = males + 1
  else:
    female_thalach = female_thalach + df['thalach'][i]
    females = females + 1

avg_male_thalach = round(male_thalach/males,2)
avg_female_thalach = round(female_thalach/females,2)

male_exang = 0
female_exang = 0
males = 0
females = 0

for i in range(0,302,1):
  if df['sex'][i] == 1:
    male_exang = male_exang + df['exang'][i]
    males = males + 1
  else:
    female_exang = female_exang + df['exang'][i]
    females = females + 1

avg_male_exang = round(male_exang/males ,4)
avg_female_exang = round(female_exang/females,4)

male_oldpeak = 0
female_oldpeak = 0
males = 0
females = 0


for i in range(0,302,1):
  if df['sex'][i] == 1:
    male_oldpeak = male_oldpeak + df['oldpeak'][i]
    males = males + 1
  else:
    female_oldpeak = female_oldpeak + df['oldpeak'][i]
    females = females + 1

avg_male_oldpeak = round(male_oldpeak/males ,4)
avg_female_oldpeak = round(female_oldpeak/females,4)

male_slope = 0
female_slope = 0
males = 0
females = 0


for i in range(0,302,1):
  if df['sex'][i] == 1:
    male_slope = male_slope + df['slope'][i]
    males = males + 1
  else:
    female_slope = female_slope + df['slope'][i]
    females = females + 1

avg_male_slope = round(male_slope/males ,3)
avg_female_slope = round(female_slope/females,3)

male_ca = 0
female_ca = 0
males = 0
females = 0
for i in range(0,302,1):
  if df['sex'][i] == 1:
    male_ca = male_ca + df['ca'][i]
    males = males + 1
  else:
    female_ca = female_ca + df['ca'][i]
    females = females + 1

avg_male_ca = round(male_ca/males ,4)
avg_female_ca = round(female_ca/females ,4)

male_thal = 0
female_thal = 0
males = 0
females = 0


for i in range(0,302,1):
  if df['sex'][i] == 1:
    male_thal = male_thal + df['thal'][i]
    males = males + 1
  else:
    female_thal = female_thal + df['thal'][i]
    females = females + 1

avg_male_thal = round(male_thal/males ,3)
avg_female_thal = round(female_thal/females, 3)

avg = {'avg_age' : [avg_male_age,avg_female_age],
       'sex' : [1,0],
          'avg_cp' : [avg_male_cp, avg_female_cp],
          'avg_trestbps' : [avg_male_trbps, avg_female_trbps],
          'avg_chol' : [avg_male_chol, avg_female_chol],
          'avg_fbs' : [avg_male_fbs, avg_female_fbs ],
          'avg_restecg' : [avg_male_ecg, avg_female_ecg],
          'avg_thalach' : [avg_male_thalach, avg_female_thalach],
          'avg_exang' : [avg_male_exang, avg_female_exang],
          'avg_oldpeak' : [avg_male_oldpeak, avg_female_oldpeak],
          'avg_slope' : [avg_male_slope, avg_female_slope],
          'avg_ca' : [avg_male_ca, avg_female_ca],
          'avg_thal' : [avg_male_thal, avg_female_thal] }

avg_df = pd.DataFrame(avg, index = ['Male', 'Female'])

model = joblib.load('HeartDiseasePrediction')
st.title("""
Heart Disease Prediction App
This App Predicts The Chances of a **Heart Disease** based on a Person's Medical Report
"""
)
op =[None]*13
ip = st.number_input('Enter the Age')
op[0] = ip
ip2 = st.number_input('Enter the sex[0 for Female, 1 for Male]')
op[1] = ip2
ip3 = st.number_input('Enter the chest pain type[4 values]')
op[2] = ip3
ip4 = st.number_input('Enter The resting blood pressure')
op[3] = ip4
ip5 = st.number_input('Enter the cholestrol level')
op[4] = ip5
ip6 = st.number_input('Enter the fasting blood sugar')
op[5] = ip6
ip7 = st.number_input('Enter the resting electrocardiographic results(values 0,1,2)')
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

pred_var = model.predict([op])
if st.button("Predict"):
  if pred_var == 1:
    st.write("Person has **Higher** Chance of Heart Disease")
    st.bar_chart(avg_df,use_container_width=True)
    st.bar_chart(op,use_container_width=True)
  else:
    st.balloons()
    st.write("Person has **Lower** Chance of Heart Disease")
    st.bar_chart(avg_df,use_container_width=True)
    st.bar_chart(op,use_container_width=True)
