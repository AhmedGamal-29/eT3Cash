#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install yfinance scikit-learn pandas matplotlib


# In[1]:


import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error



# In[3]:


# Define the stock tickers
tickers = ['GOOGL', 'AAPL', 'TSLA']  # Add the ticker for Jewelry stock if available
data = {}

# Download historical data for each stock
for ticker in tickers:
    data[ticker] = yf.download(ticker, period="3mo", interval="1d")




# In[4]:


# Prepare the data for training
def prepare_data(ticker_data):
    ticker_data['Date'] = ticker_data.index
    ticker_data['Previous Close'] = ticker_data['Close'].shift(1)  # Previous day's price as feature
    ticker_data = ticker_data.dropna()  # Drop rows with missing values
    return ticker_data[['Previous Close', 'Close']]  # Features: Previous Close, Target: Close

# Prepare data for each stock
prepared_data = {ticker: prepare_data(data[ticker]) for ticker in tickers}



# In[5]:


# Train a Linear Regression model for each stock
models = {}
for ticker, ticker_data in prepared_data.items():
    X = ticker_data[['Previous Close']]  # Previous day's price as input feature
    y = ticker_data['Close']  # Today's closing price as target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)  # 80% training, 20% testing
    
    # Initialize and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Store the trained model
    models[ticker] = model
    
    # Predict the stock prices for the test data
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)  # Calculate MAE for model evaluation
    print(f"{ticker} - Mean Absolute Error: {mae:.2f}")
    
    # Plot the actual vs predicted stock prices
    plt.figure(figsize=(10,6))
    plt.plot(y_test.index, y_test, label="True Prices", color='blue')
    plt.plot(y_test.index, y_pred, label="Predicted Prices", color='red')
    plt.title(f"{ticker} Stock Price Prediction (Linear Regression)")
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.legend()
    plt.show()



# In[13]:


# Predict the next day's stock prices
for ticker, model in models.items():
    last_close = data[ticker]['Close'].iloc[-1]  # Get the last closing price
    
    # Ensure the input is a 2D array with shape (1, 1)
    next_day_prediction = model.predict(np.array([[last_close]]).reshape(1, -1))  # Reshape to 2D array (1, 1)
    
    # Extract the scalar value from the prediction
    predicted_price = next_day_prediction[0][0]  # Get the scalar value from the 2D array
    
    # Print the result
    print(f"Next day's predicted price for {ticker}: ${predicted_price:.2f}")


# In[ ]:




