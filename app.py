import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="GME Rocket 🚀", layout="wide")

st.title("GME Rocket: Price vs Max Pain 🚀")

# Download GME price data
ticker = "GME"
data = yf.download(ticker, period="6mo", interval="1d")

# Mock max pain (replace this later with real data)
data['Max Pain'] = data['Close'].rolling(window=5).mean()

# Plot
fig, ax = plt.subplots()
ax.plot(data.index, data['Close'], label='GME Price', color='green')
ax.plot(data.index, data['Max Pain'], label='Max Pain', color='blue')
ax.fill_between(data.index, data['Close'], data['Max Pain'], where=(data['Close'] > data['Max Pain']), color='green', alpha=0.3)
ax.fill_between(data.index, data['Close'], data['Max Pain'], where=(data['Close'] < data['Max Pain']), color='red', alpha=0.3)
ax.legend()
st.pyplot(fig)
