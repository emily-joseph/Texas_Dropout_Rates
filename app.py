import streamlit as st
import pickle
from collections import namedtuple

loaded_model = pickle.load(open("mymodel (1).sav", 'rb'))

st.text("This is an app that predicts dropout rate based on inputed factors")

ecnr = st.number_input('Enter campus economically disadvantaged annual dropout rate:', 0, 74)
st.text(ecnr)
malr = st.number_input('Enter the campus male annual dropout rate:', 0, 76)
st.text(malr)
ovrr = st.number_input('Enter the campus overage annual dropout rate:', 0, 76)
st.text(ovrr)
femr = st.number_input('Enter the campus female annual dropout rate:', 0, 44)
st.text(femr)
whr = st.number_input('Enter the campus White annual dropout rate:', 0, 77)
st.text(whr)
hsr = st.number_input('Enter the campus Hispanic annual dropout rate:', 0, 72)
st.text(hsr)
necr = st.number_input('Enter the campus not economically disadvantaged annual dropout rate', 0, 58)
st.text(necr)
cter = st.number_input('Enter the campus career and technical education annual dropout rate', 0, 75)
st.text(cter)
atrr = st.number_input('Enter the campus at-risk annual dropout rate', 0, 67)
st.text(atrr)
aar = st.number_input('Enter the campus African American annual dropout rate', 0, 76)
st.text(aar)

response = loaded_model.predict([[ecnr,malr,ovrr,femr,whr,hsr,necr,cter,atrr,aar]])
st.text(f"The dropout rate will be:{response}")
