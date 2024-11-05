import eda, predict
import streamlit as st

navigation = st.sidebar.selectbox('Navigation', ['EDA', 'House Pricing Prediction'])

st.sidebar.markdown('# About')
st.sidebar.write('''This application assists company in finding improvement
                 and update Genshin Impact for better experience''')

if navigation == 'EDA':
    eda.run()
else:
    predict.run()