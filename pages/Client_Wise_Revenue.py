# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 12:15:03 2023

@author: aspirex99
"""
import streamlit as st
#import pandas as pd
import plotly.express as px

df = st.session_state['df']
st.header('Client wise Revenue')
upto = st.sidebar.slider('Top Customers',min_value = 0,max_value=50)
to = st.sidebar.slider('Bottom Customers',min_value = 0,max_value=50)

revenue_data = df[['Clients','Revenue (in Rs.) (April 2022 to till date)']]


fig = px.pie(revenue_data, values='Revenue (in Rs.) (April 2022 to till date)', names='Clients',hover_name='Clients', 
             hole=0.7)
fig.update_traces(textposition='inside', textinfo='percent',textfont=dict(size=13))
st.plotly_chart(fig)

st.header('Top Client Revenue')
new_revenue_data = revenue_data[revenue_data['Revenue (in Rs.) (April 2022 to till date)'] > 0]
top = revenue_data.reset_index(drop=True).sort_values(by='Revenue (in Rs.) (April 2022 to till date)',ascending=False).iloc[:upto,:]

fig = px.pie(top, values='Revenue (in Rs.) (April 2022 to till date)', names='Clients',hover_name='Clients', 
             hole=0.7)
fig.update_traces(textposition='outside', textinfo='label',textfont=dict(size=13))
st.plotly_chart(fig)

st.header('Bottom Client Revenue')

least =new_revenue_data.reset_index(drop=True).sort_values(by='Revenue (in Rs.) (April 2022 to till date)',ascending=True).iloc[:to,:]
fig = px.pie(least, values='Revenue (in Rs.) (April 2022 to till date)', names='Clients',hover_name='Clients', 
             hole=0.7)
fig.update_traces(textposition='outside', textinfo='label',textfont=dict(size=13))
st.plotly_chart(fig)


