import streamlit as st
import requests
import json

st.title("Test Assignment.")

# Retrieving the 20 most recent announcements for each ticker
ticker = ["AEE","REZ","1AE","1MC","NRZ"]
recent_announcements = {} # creat empty dictionary 
for i in range(len(ticker)): # roop
    def fetch_announcements(ticker): # load the data based on the ticker symbol
        url = f"https://www.asx.com.au/asx/1/company/{ticker}/announcements?count=20&market_sensitive=false"
        response = requests.get(url)
        response_json = json.loads(response.text)
        return response_json
    
    result = fetch_announcements(ticker[i]) # call the function based on the tcker symbol
    for doc_release in result['data']: # the roop to append the selected announcements
        if doc_release['issuer_code'] in recent_announcements:
            recent_announcements[doc_release['issuer_code']].append(doc_release['id'])
        else:
            recent_announcements[doc_release['issuer_code']] = []
            recent_announcements[doc_release['issuer_code']].append(doc_release['id'])


st.subheader("The 20 most recent announcements for each ticker (announcement id's):")
st.data_editor(recent_announcements) # update/report the result into stremlit application 


#Implementing a functionality that allows users to filter and view announcements by selecting 
#the ticker symbol.
st.subheader("Filtering and viewing announcements by selecting the ticker symbol.")

@st.cache_data # speed up data loading
def load_data(ticker): # load the data
    url1 = f"https://www.asx.com.au/asx/1/company/{ticker}/announcements?count=20&market_sensitive=false"
    response1 = requests.get(url1)
    response_json1 = json.loads(response1.text)
    return response_json1

symbol = ["AEE","REZ","1AE","1MC","NRZ"] # symbols to be selected
select_ticker_symbol = st.selectbox("Select a symbol", symbol)
if select_ticker_symbol: # lood to display the selected symbol
    symbol_selected = load_data(select_ticker_symbol)
    st.data_editor(symbol_selected)


#Implementing a functionality to identify and display tickers that have a 
#"Trading Halt" announcement in their recent announcements.
st.subheader("The tickers that have a Trading Halt announcement are:")
ticker = ["AEE","REZ","1AE","1MC","NRZ"]
halt = [] # store the selected ticker
for i in range(len(ticker)):# loop to select a ticker
    def fetch_announcements(ticker): # function that load data
        url = f"https://www.asx.com.au/asx/1/company/{ticker}/announcements?count=20&market_sensitive=false"
        response = requests.get(url)
        response_json = json.loads(response.text)
        return response_json

    result = fetch_announcements(ticker[i])
    #print(result['data'])
    for doc_release in result['data']:
        if doc_release['header'] == "Trading Halt":# the condition to check ticker with Trading halt
            halt.append(ticker[i])

st.data_editor(halt) # display it in streamlit application
