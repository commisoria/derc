import yfinance as yf
import pandas as pd
from binance.client import Client
from datetime import time,datetime
import numpy as np
import streamlit as st
import requests

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
api_key='9WY9XfdvHWcCcN9Gn3ajwipyNNMK10DXU3HcodLxPyMbQJ5R4Gg1VbdApH0W9cZD'
api_secret='bYWcoKb4iEz6GWRORww970rdsLsvWdEOGNFEJ2Zsr2CqrAqCf4ICEnKsqLhDnkV9'
client=Client(api_key=api_key,api_secret=api_secret)
# Get account information
account_info = client.get_account()

# Find the balance for PAXG
for balance in account_info['balances']:
    if balance['asset'] == 'PAXG':
        st.write(balance['free'])









