import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from keras.layers import Dense, Dropout, LSTM
from keras.models import Sequential
from keras.models import load_model
import streamlit as st





#describing data

start = '2013-01-01'
end = '2021-12-31'
st.title('stock trend ')
user_input = st.text_input('Enter stock ticker', 'AAPL')
df = data.DataReader(user_input  , 'yahoo' , start , end)
st.subheader('Data from 2013-2021')
st.write(df.describe())

#visualization

st.subheader('Closing price VS Time chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close, 'r')
st.pyplot(fig)
plt.style.use('dark_background')


st.subheader('Closing price VS Time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close, 'r')
plt.plot(ma100, 'y')
st.pyplot(fig)

plt.style.use('dark_background')

st.subheader('Closing price VS Time chart with 100MA & 200MA')
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close, 'r')
plt.plot(ma100, 'y')
plt.plot(ma200, 'g')
st.pyplot(fig)

data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

scaler = MinMaxScaler(feature_range = (0,1))
data_training_array = scaler.fit_transform(data_training)




#loading model

model = load_model('keras_model.h5')

#testing part

past_100_days = data_training.tail(100)
final_df = past_100_days.append(data_testing, ignore_index = True)
input_data = scaler.fit_transform(final_df)

x_test = []
y_test = []

for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i-100: i])
    y_test.append(input_data[i, 0])

x_test, y_test = np.array(x_test), np.array(y_test)
y_predicted = model.predict(x_test)

scaler = scaler.scale_

scale_factor = 1/scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor


#Final graph

st.subheader('Prediction vs Original')
fig2 =plt.figure(figsize=(12,6))
plt.plot(y_test, 'b', label = 'Original Price')
plt.plot(y_predicted, 'r', label = 'Predicted Price')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
st.pyplot(fig2)

col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    button1 = st.button('Buy')
with col4:
  pass

with col5:
    pass
with col3 :

    
    button2 = st.button('Sell')


