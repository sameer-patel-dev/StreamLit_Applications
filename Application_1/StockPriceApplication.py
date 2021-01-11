import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price Application using StreamLit
## - Developed By Sameer Patel

### Shown are the stock **closing price** and ***volume*** of Google, Apple and Amazon!

""")

#define the ticker symbol
tickerSymbol1 = 'GOOGL'
tickerSymbol2 = 'AAPL'
tickerSymbol3 = 'AMZN'

#get data on this ticker
tickerData1 = yf.Ticker(tickerSymbol1)
#get the historical prices for this ticker
tickerDf1 = tickerData1.history(period='1d', start='2010-5-31', end='2020-5-31')

#get data on this ticker
tickerData2 = yf.Ticker(tickerSymbol2)
#get the historical prices for this ticker
tickerDf2 = tickerData2.history(period='1d', start='2010-5-31', end='2020-5-31')

#get data on this ticker
tickerData3 = yf.Ticker(tickerSymbol3)
#get the historical prices for this ticker
tickerDf3 = tickerData3.history(period='1d', start='2010-5-31', end='2020-5-31')


st.write("""
# GOOGLE
### Closing Price
""")
st.line_chart(tickerDf1.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf1.Volume)

st.write("""
# APPLE
### Closing Price
""")
st.line_chart(tickerDf2.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf2.Volume)

st.write("""
# AMAZON
### Closing Price
""")
st.line_chart(tickerDf3.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf3.Volume)
