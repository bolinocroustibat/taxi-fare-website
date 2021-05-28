import datetime
import json
import requests
import streamlit as st

'''
# NY taxi fare predictor
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

date = st.date_input("Date of pickup:", value=datetime.datetime.now(), min_value=None, max_value=None, key=None, help=None)

time = st.time_input("Time of pickup:", datetime.datetime.now())

pickup_datetime = datetime.datetime.strptime(f"{date} {time.hour}:{time.minute}:{time.second}", '%Y-%m-%d %H:%M:%S')

pickup_longitude: float = st.number_input('Pickup longitude:', value=40.7614327)

pickup_latitude: float = st.number_input('Pickup latitude:', value=-73.9798156)

dropoff_longitude: float = st.number_input('Dropoff longitude:', value=40.6513111)

dropoff_latitude: float = st.number_input('Dropoff latitude:', value=-73.8803331)

passenger_count: int = st.number_input('Number of passengers:', min_value=1, max_value=6, value=1, step=1)

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

url = 'https://taxifare-api-dmdkbp3odq-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

# '''

# 2. Let's build a dictionary containing the parameters for our API...

# 3. Let's call our API using the `requests` package...

# 4. Let's retrieve the prediction from the **JSON** returned by the API...

# ## Finally, we can display the prediction to the user
# '''

params: dict = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}
response_content = requests.get(url, params=params).content

result: float = round(json.loads(response_content)["result"], 2)

st.title(f"The taxi price would be {result} $")
