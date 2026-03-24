import streamlit as st
import pickle
model=pickle.load(open("model.pkl",'rb'))
st.title("Rent Prediction App")
bhk=st.number_input("enter BHK",min_value=0,max_value=7,value=1)
size=st.number_input("enter Size",min_value=0,max_value=50000,value=1)

if st.button("Predict"):
    result=model.predict([[bhk,size]])
    st.write(f'Predicted Rent: {int(result[0])}')