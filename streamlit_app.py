import os
import time
import datetime

import numpy as np
import altair as alt
import pandas as pd

import streamlit as st


# set_page_config() can only be called once per app page, and must be called as the first Streamlit command in your script.
st.set_page_config(layout="wide")


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
    value=(datetime.time(11, 30), datetime.time(12, 45)))
st.write("You're scheduled for:", appointment)

st.subheader('Datetime slider')
start_time = st.slider(
    "When do you start?",
    datetime.datetime(2000, 1, 1), datetime.datetime(
        2050, 1, 1), datetime.datetime(2025, 1, 1),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

start_time = st.slider(
    "When do you start?",
    value=datetime.datetime(2020, 1, 1, 9, 30),
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
st.write('What would you like to order?')
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

st.title('st.secrets')
st.write('st.secrets[message]:', st.secrets['message'])
st.write(
    "Has environment variables been set:",
    os.environ["USER"] == st.secrets['username'])


st.title('st.file_uploader')
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info('☝️ Upload a CSV file')


st.title('How to layout your Streamlit app')
with st.expander('About this app(st.expander)'):
    st.write(
        'This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input(st.sidebar)')
user_name = st.sidebar.text_input('What is your name?(st.sidebar.text_input)')
user_emoji = st.sidebar.selectbox(
    'Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', [
                                 '', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])
st.header('Output(st.columns)')
col1, col2, col3 = st.columns(3)
with col1:
    if user_name != '':
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write('👈  Please enter your **name**!')
with col2:
    if user_emoji != '':
        st.write(f'{user_emoji} is your favorite **emoji**!')
    else:
        st.write('👈 Please choose an **emoji**!')
with col3:
    if user_food != '':
        st.write(f'🍴 **{user_food}** is your favorite **food**!')
    else:
        st.write('👈 Please choose your favorite **food**!')

st.title('st.progress')
my_bar = st.progress(0)
for percent_complete in range(10):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1)
st.balloons()

###################################################################################################
st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox(
        'Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox(
        'Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox(
        'Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider(
        'Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')

# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)


###################################################################################################
st.title('st.experimental_get_query_params')

# 1. Instructions
st.header('1. Instructions')
st.markdown('''
In the above URL bar of your internet browser, append the following:
`?name=Jack&surname=Beanstalk`
after the base URL `http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/`
such that it becomes
`http://share.streamlit.io/dataprofessor/st.experimental_get_query_params/?firstname=Jack&surname=Beanstalk`
''')


# 2. Contents of st.experimental_get_query_params
st.header('2. Contents of st.experimental_get_query_params')
st.write(st.query_params)


# 3. Retrieving and displaying information from the URL
st.header('3. Retrieving and displaying information from the URL')

try:
    firstname = st.query_params['firstname']
    surname = st.query_params['surname']

    st.write(f'Hello **{firstname} {surname}**, how are you?')
except Exception as e:
    st.info(e)


###################################################################################################
st.title('st.cache')

# Not using cache
b0 = time.time()
st.subheader('Not using st.cache_data')


def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
    )
    return df


load_data_b()
b1 = time.time()
st.info(b1-b0)

# Using cache
a0 = time.time()
st.subheader('Using st.cache_data')


@st.cache_data()
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
    )
    return df


load_data_a()
a1 = time.time()
st.info(a1-a0)

###################################################################################################
st.title('st.session_state')


def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046


def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046


st.header('Input')
col1, spacer, col2 = st.columns([2, 1, 2])
with col1:
    pounds = st.number_input("Pounds:", key="lbs", on_change=lbs_to_kg)
with col2:
    kilogram = st.number_input("Kilograms:", key="kg", on_change=kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)

###################################################################################################
st.title('st.metric')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="用户数", value=1200, delta="+50")
with col2:
    st.metric(label="活跃率", value="67%", delta="-3%")
with col3:
    st.metric(label="收入", value="$8000", delta="+$500")

###################################################################################################
