

import streamlit as st 
import requests

from datetime import date 
from plotly import graph_objs as go 
from prophet import Prophet 
from prophet.plot import plot_plotly
import yfinance as yf
from datetime import datetime, timedelta
from datetime import datetime
import pandas_datareader as pdr
import matplotlib.pyplot as plt

#st.set_page_config(page_title='Stock Price Analysis', page_icon=':chart_with_upwards_trend:')

import yfinance as yf
import datetime
import yfinance as yf
import datetime




#def get_data(ticker):
    #start_date = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d")
    #end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    #data = yf.download(ticker, start=start_date, end=end_date)
    #return data

#def forecast(ticker):
    #data = get_data(ticker)
    # perform forecasting analysis on data here
    #forecast_results = forecast(ticker)
    #return forecast_results

import datetime
import yfinance as yf
import streamlit as st
import requests
import json
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA


import datetime
import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.graph_objs as go

from prophet import Prophet
from prophet.plot import plot_plotly
from PIL import Image

#st.sidebar.header("STOCK MARKET S&P 500 PREDICTOR")

#option=st.sidebar.selectbox("Select one of the following",["STOCK MARKET FORECAST","100MA","200MA" ])
#if option=='STOCK MARKET FORECAST': 
    #st.write("")
#elif option=='100MA':
    #st.write("something ")
#elif option=='200MA':
    #st.write("hello")

    



import streamlit as st
from PIL import Image
import yfinance as yf
import datetime
import requests
import plotly.graph_objs as go
from prophet import Prophet
from prophet.plot import plot_plotly


# Set the title and image in the sidebar
st.sidebar.title('STOCK MARKET PREDICTION APP')
options = ['STOCK TREND FORECAST', 'ABOUT THE APP', 'PREDICTOR EXPLAINED']
selected_option = st.sidebar.selectbox('Select an option', options)


import streamlit as st
import datetime
import pandas as pd
import plotly.graph_objects as go
from prophet import Prophet
from yahooquery import Ticker
import requests




import datetime
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from yahooquery import Ticker
from prophet import Prophet

# Function to fetch stock data
def get_data(ticker, start_date):
    try:
        stock = Ticker(ticker)
        data = stock.history(start=start_date)
        
        if data is None or data.empty:
            return None
        
        if isinstance(data.index, pd.MultiIndex):
            data = data.reset_index()
        
        if 'close' in data.columns:
            data.rename(columns={'close': 'Close'}, inplace=True)
        
        data['Date'] = pd.to_datetime(data['date'], errors='coerce')
        data.dropna(subset=['Date', 'Close'], inplace=True)
        
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Function to predict stock prices using Prophet
def predict_stock_price(data, days=30):
    df = data[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})
     # Remove timezone from ds column
    df['ds'] = df['ds'].dt.tz_localize(None)
    model = Prophet()
    model.fit(df)
    
    future = model.make_future_dataframe(periods=days)
    forecast = model.predict(future)
    
    return forecast

# Streamlit UI
st.title('Stock Market Predictor')

ticker = st.sidebar.text_input("Enter a stock ticker symbol (e.g. AAPL):", "AAPL")
start_date = (datetime.datetime.now() - datetime.timedelta(days=365)).strftime("%Y-%m-%d")

# Fetch latest stock data
data = get_data(ticker, start_date)

if data is not None and 'Close' in data.columns:
    st.subheader('Raw Data')
    st.write(data.tail())
    
    st.subheader('Closing Price vs Time Chart')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock Close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    
    if len(data) >= 100:
        st.subheader('Closing Price vs Time Chart with 100 MA')
        ma100 = data['Close'].rolling(100).mean()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=ma100, name='100-day Moving Average', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock Close', line=dict(color='green')))
        fig.layout.update(title_text="Time Series Data with 100-day Moving Average", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)
    
    if len(data) >= 200:
        st.subheader('Closing Price vs Time Chart with 100MA & 200MA')
        ma100 = data['Close'].rolling(100).mean()
        ma200 = data['Close'].rolling(200).mean()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=ma100, name='100-day Moving Average', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=data['Date'], y=ma200, name='200-day Moving Average', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Stock Close', line=dict(color='green')))
        fig.layout.update(title_text="Time Series Data with 100-day & 200-day Moving Averages", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)
    
    # Prophet Prediction
    st.subheader('Stock Price Prediction')
    try:
        forecast = predict_stock_price(data)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='Historical Data', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Predicted Price', line=dict(color='red')))
        fig.layout.update(title_text="Stock Price Prediction", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)
        
        # Trend Analysis
        last_actual_price = data['Close'].iloc[-1]
        last_predicted_price = forecast['yhat'].iloc[-1]
        
        if last_predicted_price > last_actual_price:
            st.success("📈 The stock price is likely to go UP based on predictions.")
        else:
            st.error("📉 The stock price is likely to go DOWN based on predictions.")
    
    except Exception as e:
        st.error(f"Error generating prediction: {e}")
else:
    st.error("No valid data available for the selected ticker.")










    

# ABOUT section
if selected_option == 'ABOUT THE APP':
    st.sidebar.subheader('ABOUT THE APP')
    st.title('ABOUT THE APP')

    st.write('The stock trend predictor is a powerful tool that utilizes historical stock market data to forecast the future price trend of a specific stock. These predictions can assist investors and traders in making informed decisions and developing effective investment strategies.')
    st.write('Disclaimer: The stock trend predictor is for informational purposes only and should not be considered as financial advice. Investing in the stock market involves risks, and decisions based on the predictions should be made at your own discretion. Always consult with a qualified financial advisor before making any investment decisions.')
    
    
    



# DEFINITIONS section
elif selected_option == 'PREDICTOR EXPLAINED':
    st.sidebar.subheader('MAIN CONCEPTS')
    st.title('PREDICTOR EXPLAINED')
   

    
 
    st.subheader('Stock Market')
    st.write("The stock market refers to a marketplace where buyers and sellers trade shares of publicly listed companies. It is a platform where investors can buy or sell stocks, bonds, and other securities.")
    st.write("The stock market provides companies with a means to raise capital by issuing shares to investors in exchange for ownership. Investors, on the other hand, can participate in the stock market to potentially earn profits by buying stocks at a lower price and selling them at a higher price.")
    st.write("Stock markets play a crucial role in the economy, as they enable companies to raise funds for expansion and provide individuals with opportunities to invest and grow their wealth. They are influenced by various factors, including economic conditions, company performance, investor sentiment, and global events.")


    st.subheader('Closing Price vs Time Chart')
    st.write("A Closing Price vs Time Chart is a graphical representation of a stock's closing prices over a specific period of time. It shows the historical trend of a stock's closing prices, which is the price at which the stock traded at the end of each trading day.")
    st.write("The x-axis of the chart represents the time period, typically in days, months, or years, depending on the selected timeframe. The y-axis represents the stock's closing prices. Each data point on the chart corresponds to the closing price of the stock at a specific point in time.")
    st.write("This type of chart is commonly used to visually analyze the price movements and trends of a stock over time. It helps investors and traders identify patterns, support and resistance levels, and potential buying or selling opportunities based on historical price behavior.")

# Closing Price vs Time Chart with 100MA definition

    st.subheader('Closing Price vs Time Chart with 100MA')
    st.write("A Closing Price vs Time Chart with 100MA is a graphical representation of a stock's closing prices along with its 100-day Moving Average (MA) over a specific period of time. It combines the historical trend of the stock's closing prices with a smoothed line that represents the average price over the past 100 days.")
    st.write("The chart displays the stock's closing prices as data points, typically represented by dots or markers, connected by a line. Additionally, it includes a line plot representing the 100-day Moving Average, which is calculated by taking the average closing price over the past 100 trading days.")
    st.write("The Closing Price vs Time Chart with 100MA is useful for visualizing the stock's price movements over time and identifying the overall trend. The 100-day Moving Average helps smoothen out short-term fluctuations and provides a clearer picture of the stock's long-term trend.")
    st.write("Investors and traders often use this chart to assess the stock's current price relative to its historical performance and to identify potential buying or selling opportunities based on the interaction between the stock's closing prices and the 100-day Moving Average.")

# Closing Price vs Time Chart with 100MA and 200MA definition

    st.subheader('Closing Price vs Time Chart with 100MA & 200MA')
    st.write("A Closing Price vs Time Chart with 100MA and 200MA is a graphical representation of a stock's closing prices along with its 100-day Moving Average (100MA) and 200-day Moving Average (200MA) over a specific period of time. It provides insights into the stock's historical price movements and long-term trends.")
    st.write("The chart displays the stock's closing prices as data points, typically represented by dots or markers, connected by a line. Additionally, it includes two line plots representing the 100-day Moving Average and the 200-day Moving Average. The 100MA is calculated by taking the average closing price over the past 100 trading days, while the 200MA is calculated over the past 200 trading days.")
    st.write("The Closing Price vs Time Chart with 100MA and 200MA is useful for identifying the stock's long-term trend and potential support and resistance levels. It helps smooth out short-term price fluctuations and provides a clearer picture of the stock's overall price movements.")
    st.write("Investors and traders often analyze this chart to assess the stock's current price relative to its moving averages. Crosses between the stock's closing price and the moving averages can indicate potential trend reversals or confirm the prevailing trend. The chart's visualization aids in making informed decisions about buying, selling, or holding the stock.")
    st.write("When the 100MA is above the 200MA:")
    st.write("- This is known as a 'bullish crossover' or a 'golden cross.'")
    st.write("- It suggests a potential shift to a bullish trend in the stock.")
    st.write("- The 100MA, representing the shorter-term average, crossing above the 200MA, representing the longer-term average, indicates positive momentum.")
    st.write("- It is often considered a bullish signal by technical analysts and may attract more buyers into the market.")
    st.write("When the 100MA is below the 200MA:")
    st.write("- This is known as a 'bearish crossover' or a 'death cross.'")
    st.write("- It suggests a potential shift to a bearish trend in the stock.")
    st.write("- The 100MA, representing the shorter-term average, crossing below the 200MA, representing the longer-term average, indicates negative momentum.")
   
    st.write("- It is often considered a bearish signal by technical analysts and may prompt more selling pressure in the market.")
# Closing Price vs Time Chart with 100MA and 200MA definition

    st.subheader('Closing Price vs Time Chart with 100MA & 200MA Representation')
    st.write("Here are some scenarios to consider:")
    st.write("When the Closing Price is above the 100MA and the 100MA is above the 200MA:")
    st.write("- This indicates a potentially bullish trend. The stock's recent average price (100MA) is higher than its longer-term average price (200MA), suggesting positive momentum.")
    st.write("- The upward separation between the lines suggests strength in the stock's price movement, with the 100MA serving as potential support during pullbacks.")

    st.write("When the Closing Price is below the 100MA and the 100MA is below the 200MA:")
    st.write("- This indicates a potentially bearish trend. The stock's recent average price (100MA) is lower than its longer-term average price (200MA), suggesting negative momentum.")
    st.write("- The downward separation between the lines suggests weakness in the stock's price movement, with the 100MA acting as potential resistance during rallies.")

    st.write("When the Closing Price crosses above or below the 100MA or 200MA:")
    st.write("- These crossovers can indicate potential trend reversals. For example, if the Closing Price crosses above the 100MA or 200MA, it may signal a shift from a downtrend to an uptrend.")
    st.write("- These crossovers can also serve as confirmation of the prevailing trend. If the Closing Price remains consistently above the 100MA and 200MA, it suggests a sustained bullish trend.")


    
    # Market Capitalization definition
    st.subheader('Market Capitalization (Market Cap)')
    st.write("Market capitalization, also known as market cap, is a measure of a company's total market value. It represents the current market price of a company's outstanding shares multiplied by the total number of shares outstanding.")
    st.write("Market cap is used to categorize companies based on their size and value. It provides investors with an idea of the company's relative worth and is an important factor considered by investors when making investment decisions.")
    st.write("Typically, companies with higher market capitalizations are considered larger and more established, while those with lower market capitalizations are considered smaller and potentially higher growth opportunities.")
    st.write("Market cap is calculated by multiplying the company's current stock price by the total number of shares outstanding. It can be categorized into different tiers, such as large-cap, mid-cap, and small-cap, based on predefined market cap ranges.")
    st.write("Investors often use market capitalization as one of the factors in their investment analysis and portfolio diversification strategies. It helps them assess the risk and potential return associated with different types of companies.")

##In summary, the required rate of return and the valuation of an investment are inversely related. A higher required rate of return implies a higher perceived risk, leading to a lower valuation, while a lower required rate of return suggests lower perceived risk, resulting in a higher valuation.




    st.title('Valuation')

    # Growth definition
    st.subheader('Growth')
    st.write("Growth refers to the rate at which a company's earnings, revenue, or other financial metrics are expected to increase over time. It is an important factor in stock valuation as investors often look for companies with strong growth potential.")

    # P/E Ratio definition
    st.subheader('P/E Ratio')
    st.write("The P/E (Price-to-Earnings) ratio is a valuation metric that compares a company's stock price to its earnings per share (EPS). It indicates how much investors are willing to pay for each dollar of earnings generated by the company. A higher P/E ratio suggests a higher valuation relative to earnings.")

    # Required Rate of Return definition
    st.subheader('Required Rate of Return')
    st.write("The required rate of return is the minimum return that an investor expects to earn from an investment. It is influenced by factors such as the investor's risk tolerance, market conditions, and the perceived risk of the stock. The required rate of return helps determine the fair value of a stock.")

    # EPS definition
    st.subheader('EPS (Earnings per Share)')
    st.write("EPS is a financial metric that represents a company's earnings divided by the number of outstanding shares. It provides information about a company's profitability on a per-share basis and is used in various valuation methods.")
    st.write("Higher EPS generally indicates higher profitability, as it suggests that the company is generating more earnings relative to its number of shares.")
    st.write("However, it's important to consider EPS in conjunction with other factors such as industry norms, growth prospects, and historical performance to get a comprehensive understanding of a company's financial health and potential investment value.")
    # Future Price definition
    st.subheader('Future Price')
    st.write("The future price is the expected price of a stock at a specific point in the future. It is often estimated based on growth projections, industry trends, and market conditions. The future price is used in valuation models to determine the potential upside or downside of a stock.")

    # Sticker Price definition
    st.subheader('Sticker Price')
    st.write("The sticker price is an estimated fair value or target price for a stock based on valuation models and analysis. It represents the price at which the stock is considered fairly valued.")

    # Current Price definition
    st.subheader('Current Price')
    st.write("The current price is the actual market price at which a stock is currently trading. It reflects the supply and demand dynamics in the market and may differ from the stock's intrinsic value.")

    # Upside definition
    st.subheader('Upside')
    # Upside definition

    st.write("Upside refers to the potential price appreciation or gain that a stock may experience in the future.")
    st.write("It is calculated as the percentage difference between the estimated fair value (sticker price) and the current price.")
    st.write("A positive upside indicates that the estimated fair value exceeds the current price, suggesting potential price appreciation and a potential gain for investors.")
    st.write("Conversely, a negative upside would indicate that the estimated fair value is lower than the current price, suggesting a potential price decline and a potential loss for investors.")


    st.subheader("Sticker Price < Current Price < Future Price:")
    st.write("The stock is potentially undervalued based on the estimated fair value.")
    st.write("The future price is higher than the current price, indicating potential price appreciation.")
    st.write("This creates a potential investment opportunity.")
    st.subheader("Current Price > Future Price:")
    st.write("The estimated future price is lower than the current price, suggesting potential downside.")
    st.subheader("Current Price < Future Price:")
    st.write("The estimated future price is higher than the current price, indicating potential upside.")
    st.write("This suggests that the stock may be undervalued or trading below its estimated fair value.")
    st.write("There is a potential for the stock's value to increase in the future, creating an investment opportunity.")
    st.write("The estimated future price is the same as the current price, suggesting no potential gain or loss.")








##This formula calculates the percentage difference between the estimated fair value (sticker price) and the current price. A positive upside indicates that the estimated fair value exceeds the current price, suggesting potential price appreciation and a potential gain for investors.

##Conversely, a negative upside would indicate that the estimated fair value is lower than the current price, suggesting a potential price decline and a potential loss for investors.

##Therefore, the formula you provided accurately represents the concept of upside in relation to the estimated fair value and the current price. could you give me a more accurate defintiion taking into account the definition you gave me before for upside 




# Upside definition
##st.subheader('Upside')
##st.write("Upside refers to the potential gain or profit expected from an investment. It represents the difference between the estimated future price and the current price, expressed as a percentage.")
##st.write("An upside of -9.53 means that the estimated future price of a stock is expected to be 9.53% lower than the current price. It suggests a potential downside or decrease in the stock's value.")
##st.write("For example, if the current price of a stock is $100, an upside of -9.53 would imply that the estimated future price is $90.47 (which is 9.53% lower than $100).")
#st.write("Upside is often considered in investment analysis to evaluate the potential return on investment and assess the risk associated with a particular stock or investment opportunity.")
##Upside is typically used as a measure of potential gain or profit. A positive upside indicates an expected increase in value, while a negative upside indicates a potential decrease in value.
