

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

CyberSecurity_LR = pickle.load(open('LogisticRegration.sav', 'rb'))

bank_prediction = pickle.load(open('classifier.pkl', 'rb'))
salary_prediction = pickle.load(open('salary_prediction.sav', 'rb'))
# Bank_Note_Aut_model = pickle.load(open('classifier.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

['with NN']

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('My Models List',
                          
                          ['Cyber Security Factors using Logistic Regration',
                           'Data Scientist Salary Prediction',
                           'Bank Note Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# CyberSecurity Logistic Regration Prediction Page
if (selected == 'Cyber Security Factors using Logistic Regration'):
    # page title
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
    
    if st.button('Salary prediction Test Result'):
        salary_predictions = salary_prediction.predict([[work_year, experience_level, employment_type, job_title,employee_residence, remote_ratio,company_location,company_size, salary_currency, salary_in_usd]])                          
        
        if (salary_predictions[0] == 1):
          Data_Scientist_Salary_prediction = 'Salary'
        else:
          Data_Scientist_Salary_prediction = 'Their is something wrong'
        
    st.success(Data_Scientist_Salary_prediction)
        
# st.text('')
# if st.button("Predict type of Iris"):
#     result = salary_prediction.predict(np.array([[work_year, experience_level, employment_type, job_title,employee_residence, remote_ratio,company_location,company_size, salary_currency, salary_in_usd]]))
#     st.text(result[0])


# st.text('')
# st.text('')    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,
                                                           APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)


    
    # code for Prediction
    Bank_Note_Auth = ''
    # Bank Note Prediction
    # creating a button for Prediction    
    if st.button("Abank Note Auth's Test Result"):
        bank_notes_prediction = bank_prediction.predict([[variance, skewness,curtosis,entropy]])                          
        
        if (bank_notes_prediction[0] == 1):
          Bank_Note_Auth = "The person has Parkinson's disease"
        else:
          Bank_Note_Auth = "The person does not have Parkinson's disease"
        
    st.success(Bank_Note_Auth)
















