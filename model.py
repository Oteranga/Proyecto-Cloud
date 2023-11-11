import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')
import seaborn as sns

sns.set_style('whitegrid')
plt.style.use("fivethirtyeight")

# For reading stock data from yahoo
from pandas_datareader.data import DataReader
import yfinance as yf
from pandas_datareader import data as pdr

yf.pdr_override()

from datetime import datetime,date
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense, LSTM
from flask import send_file
from io import BytesIO
import base64

def get_prediction(month, day):
    # get the stock data
    df = pdr.get_data_yahoo('AAPL', start='2016-01-01', end=datetime.now())
    y = df['Close'].fillna(method='ffill')
    y = y.values.reshape(-1, 1)

    # scale the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler = scaler.fit(y)
    y = scaler.transform(y)

    #print("Ingrese la fecha que desea predecir")
    today = date.today()
    year = today.year
    #month = int(input('Mes: '))
    #day = int(input('Dia: '))
    pred_date = date(year, month, day)
    # generate the input and output sequences
    n_lookback = 60  # length of input sequences (lookback period)
    n_forecast = (pred_date - today).days  # length of output sequences (forecast period)
    #print(n_forecast)

    X = []
    Y = []

    for i in range(n_lookback, len(y) - n_forecast + 1):
        X.append(y[i - n_lookback: i])
        Y.append(y[i: i + n_forecast])

    X = np.array(X)
    Y = np.array(Y)

    # fit the model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(n_lookback, 1)))
    model.add(LSTM(units=50))
    model.add(Dense(n_forecast))

    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X, Y, batch_size=32, epochs=20)

    # generate the forecasts
    X_ = y[- n_lookback:]  # last available input sequence
    X_ = X_.reshape(1, n_lookback, 1)

    Y_ = model.predict(X_).reshape(-1, 1)
    Y_ = scaler.inverse_transform(Y_)

    # organize the results in a data frame
    df_past = df[['Close']].reset_index()
    df_past.rename(columns={'index': 'Date', 'Close': 'Actual'}, inplace=True)
    df_past['Date'] = pd.to_datetime(df_past['Date'])
    df_past['Forecast'] = np.nan
    df_past['Forecast'].iloc[-1] = df_past['Actual'].iloc[-1]

    df_future = pd.DataFrame(columns=['Date', 'Actual', 'Forecast'])
    df_future['Date'] = pd.date_range(start=df_past['Date'].iloc[-1] + pd.Timedelta(days=1), periods=n_forecast)
    df_future['Forecast'] = Y_.flatten()
    df_future['Actual'] = np.nan

    results = df_past.append(df_future).set_index('Date')

    forecast_last = int(results[['Forecast']].iloc[-1])
    #print(forecast_last)

    # plot the results
    #plt.plot(results[['Actual', 'Forecast']],linewidth=2)
    plt.figure(figsize=(12,6))
    plt.title('APPLE Prediction')
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.plot(results[['Actual', 'Forecast']],linewidth=2)
    plt.legend(['Actual', 'Prediction'])
    plt.annotate(forecast_last, # this is the text
                    (pred_date,forecast_last), # these are the coordinates to position the label
                    textcoords="offset points", # how to position the text
                    xytext=(0,10), # distance from text to points (x,y)
                    ha='left') # horizontal alignment can be left, right or center
    
    # Save the plot as a PNG image in memory
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)
    
    # Clear the plot to avoid overlapping when the next request is made
    img_data = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.clf()
    return img_data
    #return send_file(img_data, mimetype='image/png', as_attachment=True, download_name='plot.png')
