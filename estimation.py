import yfinance as yf
import pandas as pd
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException, BinanceWithdrawException
from datetime import time,datetime
import numpy as np
import streamlit as st
import requests
import json

#-------------------------------------------------------------------------IP--------------------------------
def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        return response.json()['ip']
    else:
        return 'Unable to get IP address'

# Get and print the public IP address
public_ip = get_public_ip()
st.write(public_ip)
#--------------------------------------------------------------------------------------------------------------


def get_orders(pair, depth):
    response = requests.get(f'https://data.binance.com/api/v3/depth?symbol={pair}&limit={depth}')
    byte_json = response.content
    orders_json = json.loads(byte_json)
    return orders_json

st.write(get_orders('BTCBUSD', 5))






