import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.graph_objs as go

# Streamlit app title
st.title('Stock Price Analysis')

# User input for ticker symbol
tickerSymbol = st.text_input('Enter the ticker symbol', 'GOOGL')

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1y')

# Sort the DataFrame in descending order by the index (date)
tickerDf = tickerDf.sort_index(ascending=False)

# Display the data in descending order
st.subheader('Historical Stock Prices')
st.dataframe(tickerDf)

# Calculate the moving average
tickerDf['Moving Average'] = tickerDf['Close'].rolling(window=20).mean()

# Plot the closing price and moving average with Plotly
st.subheader('Stock Price and Moving Average')

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=tickerDf.index,
    y=tickerDf['Close'],
    mode='lines',
    name='Close Price'
))

fig.add_trace(go.Scatter(
    x=tickerDf.index,
    y=tickerDf['Moving Average'],
    mode='lines',
    name='20-Day Moving Average'
))

fig.update_layout(
    title=f'{tickerSymbol} Stock Price and Moving Average',
    xaxis_title='Date',
    yaxis_title='Price'
)

st.plotly_chart(fig)
