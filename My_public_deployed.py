

import pickle
import joblib
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

CyberSecurity_LR = pickle.load(open('LogisticRegration.sav', 'rb'))

bank_prediction = joblib.load(open('classifier.pkl', 'rb'))
# bank_prediction = pickle.load(open('classifierANN.pkl', 'rb'))
bank_prediction_ANN = pickle.load(open('dtree.pkl', 'rb'))
placement_prediction = joblib.load(open('PDT.sav', 'rb'))
# salary_prediction = pickle.load(open('classifierlr.h5', 'rb'))
salary_prediction = pickle.load(open('salary_prediction.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('My Models List',
                          
                          ['Bank Note Prediction',
                           'Decision Tree based Bank Note Prediction',
                           'Cyber Security Factors using Logistic Regration',
                           'Data Scientist Salary Prediction',                        
                           'Placement Prediction'],
                           default_index=0)
if (selected == 'Cyber Security Factors using Logistic Regration'):
    st.title('CyberSecurity Logistic Regration using ML')
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Gender = st.text_input('Gender')
        
    with col2:
        Education = st.text_input('Education')
    
    with col3:
        Field = st.text_input('Field')
    
    with col1:
        Computer_Category = st.text_input('Computer_Category')
    
    with col2:
        Device_Used = st.text_input('Device_Used')
    
    with col3:
        Connectivity_Used = st.text_input('Connectivity_Used')
    
    with col1:
        Purpose = st.text_input('Purpose')
    
    with col2:
        Age = st.text_input('Age')
    
    
    # code for Prediction
    CyberSecurity_LR_result = ''
    
    # creating a button for Prediction
    
    if st.button('CyberSecurity Test Result'):
        CyberSecurity_LR_prediction = LogisticRegration.predict([[Gender, Education, Field, Computer_Category, Device_Used, Connectivity_Used, Purpose, Age]])
        
        if (CyberSecurity_LR_prediction[0] == 1):
          CyberSecurity_LR_result = 'The person is +ve'
        else:
          CyberSecurity_LR_result = 'The person is -ve'
        
    st.success(CyberSecurity_LR_result)




# Data Scientist Salary Prediction Page
if (selected == 'Data Scientist Salary Prediction'):
    
    # page title
    st.title('Data Scientist Salary Prediction using Linear Regression ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        work_year = st.text_input('work_year')
        
    with col2:
        experience_level = st.text_input('experience_level')
        
    with col3:
        employment_type = st.text_input('Employment type')
        
    with col1:
        job_title = st.text_input('job_title')
        
    with col2:
        employee_residence = st.text_input('employee_residence')
        
    with col3:
        remote_ratio = st.text_input('remote_ratio')
        
    with col1:
        company_location = st.text_input('company_location')
        
    with col2:
        company_size = st.text_input('company_size')
        
    with col3:
        salary_currency = st.text_input('salary_currency')
        
    with col1:
        salary_in_usd = st.text_input('salary_in_usd')
        
            
     
    # code for Prediction
    Data_Scientist_Salary_prediction = ''
    
    # creating a button for Prediction
    if st.button("Salary prediction Test Result"):
        salary_predictions = salary_prediction.predict([[work_year, experience_level, employment_type, job_title,employee_residence, remote_ratio, company_location,company_size, salary_currency, salary_in_usd]])                          
        
        if (salary_predictions[0] == 1):
          Data_Scientist_Salary_prediction = "Counterfeit or Negative"
        else:
          Data_Scientist_Salary_prediction = "Authentic or Positive"
        
    st.success(Data_Scientist_Salary_prediction)

# Bank Note Authentication Prediction Page
if (selected == 'Bank Note Prediction'):
    # page title
    st.title('Bank Note Authentication Regression using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        variance = st.text_input('variance')
        
    with col2:
        skewness = st.text_input('skewness')
    
    with col3:
        curtosis = st.text_input('curtosis')
    
    with col1:
        entropy = st.text_input('entropy')
    
        
    # code for Prediction
    Bank_Note_Auth = ''
    # Bank Note Prediction
    # creating a button for Prediction    
    if st.button("Abank Note Auth's Test Result"):
        bank_notes_prediction = bank_prediction.predict([[variance, skewness,curtosis,entropy]])                          
        
        if (bank_notes_prediction[0] == 1):
          Bank_Note_Auth = "Counterfeit or Negative"
        else:
          Bank_Note_Auth = "Authentic or Positive"
        
    st.success(Bank_Note_Auth)
# Bank Note Authentication Prediction Page
if (selected == 'Decision Tree based Bank Note Prediction'):
    # page title
    st.title('Bank Note Authentication using Decision Tree')
    
    
    # getting the input data from the user
    col1, col2= st.columns(2)
    
    with col1:
        variance = st.text_input('variance')
        
    with col2:
        skewness = st.text_input('skewness')
    
    with col1:
        curtosis = st.text_input('curtosis')
    
    with col2:
        entropy = st.text_input('entropy')
    
        
    # code for Prediction
    Bank_Note_Auth = ''
    # Bank Note Prediction
    # creating a button for Prediction    
    if st.button("Abank Note Auth's Test Result"):
        bank_notes_prediction = bank_prediction.predict([[variance, skewness,curtosis,entropy]])                          
        
        if (bank_notes_prediction[0] == 1):
          Bank_Note_Auth = "Counterfeit or Negative"
        else:
          Bank_Note_Auth = "Authentic or Positive"
        
    st.success(Bank_Note_Auth)   
# Student Placement Prediction Page
if (selected == 'Placement Prediction'):
    # page title
    st.title('Student Placement using Decision Tree')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    # with col1:
    #     cgpa = st.text_input('cgpa')
        
    # Add a slider

    with col1:
        cgpa = st.slider("CGPA", min_value=0, max_value=8, value=0, step=1)
    with col1:
        iq = st.slider("IQ", min_value=0, max_value=400, value=0, step=1)
    # with col2:
    #     iq = st.selectbox("IQ", ["0", "1"])

    
    # with col2:
    #     iq = st.text_input('iq')
    
    # with col3:
    #     curtosis = st.text_input('curtosis')
    
    # with col1:
    #     entropy = st.text_input('entropy')
    
        
    # code for Prediction
    placement_prediction = ''
    # Bank Note Prediction
    # creating a button for Prediction    
    if st.button("placment's Test Result"):
        placement_predictions = placement_prediction.predict([[cgpa, iq]])                          
        
        if (placement_predictions[0] == 1):
          placement_prediction = "Counterfeit or Negative"
        else:
          placement_prediction = "Authentic or Positive"
        
    st.success(placement_prediction)















