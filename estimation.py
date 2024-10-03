import yfinance as yf
import pandas as pd
FROM binance.client import Client
from datetime import time,datetime
import numpy as np
import streamlit as st

import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        return response.json()['ip']
    else:
        return 'Unable to get IP address'

# Get and print the public IP address
public_ip = get_public_ip()
st.write(public_ip)





