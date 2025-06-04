import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

from datetime import time, datetime


st.header('st.write')


st.write('Hello, *World!* :sunglasses:')

st.write(1234)

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['a', 'b', 'c'])
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# c.interactive()  # streamlit 不生效
st.write(c)

st.header('st.slider')

st.subheader('Slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.subheader('Range slider')
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.subheader('Range time slider')
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

st.subheader('Datetime slider')
start_time = st.slider(
    "When do you start?",
    datetime(2000, 1, 1), datetime(2050, 1, 1), datetime(2025, 1, 1),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

color = st.select_slider(
    "Select a color of the rainbow",
    options=['r', 'g', 'b'],
)
st.write("My favorite color is", color)


st.header('st.line_chart')
st.line_chart(df)


st.header('st.selectbox')
option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green'))
st.write('Your favorite color is ', option)


st.header('st.multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)


st.header('st.checkbox')
st.write ('What would you like to order?')
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
if icecream:
    st.write("Great! Here's some more 🍦")
if coffee:
    st.write("Okay, here's some coffee ☕")
if cola:
    st.write("Here you go 🥤")


st.header('st.latex')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
