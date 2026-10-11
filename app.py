import joblib
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='Customer Churn Predictor',
    layout='wide',
    page_icon='📊'
)

st.title('Customer Churn Prediction System')
st.write('This app is designed to predict whether a customer will churn or not on giving the below inputs.')



col1, col2 = st.columns(2)


with st.form("customer_form"):
    with col1:
        tenure=st.number_input(label='Tenure(in Months)',min_value=0, max_value=100,value=12)
        Contract=st.selectbox(label='Contract',options=['Select','Month-to-month','One year','Two year'],index=0)
        Payment_Method=st.selectbox(label='PaymentMethod',options=['Select','Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
        OnlineSecurity=st.selectbox(label='OnlineSecurity',options=['Select','No','Yes','No Internet Service'])
        

    with col2:
        MonthyCharges=st.number_input(label='MonthlyCharges ($)',min_value=0)
        InternetService=st.selectbox(label='InternetService',options=['Select','Fiber optic','DSL','No Internet Service'])
        TechSupport=st.selectbox(label='TechSupport',options=['Select','No','Yes','No Internet Service'])

    submitted = st.form_submit_button(
        "Predict Churn"
    )

@st.cache_resource
def load_model():
    model=joblib.load('customer_churn_model.pkl')
    return model

df=pd.DataFrame([[tenure,MonthyCharges,Contract,InternetService,Payment_Method,TechSupport,OnlineSecurity]],columns=[
    'tenure','MonthlyCharges','Contract','InternetService','PaymentMethod','TechSupport','OnlineSecurity'
])


model=load_model()
if submitted:

    if Contract !='Select' and Payment_Method !='Select' and OnlineSecurity !='Select' and InternetService !='Select' and TechSupport !='Select':
        pred=model.predict(df)
        prob=model.predict_proba(df)
        no_churn=prob[:,0]
        churn=prob[:,1]

        if pred[0]==0:
            st.success('Low Churn Risk. Customer is predicted to stay')
            st.metric(
            label="Churn Probability",
            value=f"{churn[0]*100:.2f}%"
                )
        else:
            st.warning('High Churn Risk. Customer is predicted to leave.')
            st.metric(
            label="Churn Probability",
            value=f"{churn[0]*100:.2f}%"
                )
    else:
        st.error('Please select a valid option.')
        st.stop()