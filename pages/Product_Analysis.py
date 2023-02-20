# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:36:52 2023

@author: aspirex99
"""
import streamlit as st
import pandas as pd
import plotly.express as px

df = st.session_state['df']
st.header('Product wise Analysis')

def required_df(data,col):
    x = data[[col, 'Clients']]
    total_count = []
    percentage = []
    true_count = []
    false_count = []
    Status = []
    figures = []
    x['total_count'] = 0
    x['Percentage'] = 0
    x['Status'] = 0
    length = len(x[col])
    for i in range(length):
        if x[col][i] == True:
            true_count.append(1)
        else:
            false_count.append(1)
    for i in range(length):
        if x[col][i] == True:
            percentage.append(round(sum(true_count) / length * 100,2))
            total_count.append(len(true_count))
            Status.append('Opted')
        else:
            percentage.append(round(sum(false_count) / length *100,2))
            total_count.append(len(false_count))
            Status.append('Not Opted')
    x['Percentage'] = percentage
    x['total_count'] = total_count
    x['Status'] = Status

    df = x
    per = df['Percentage'].tolist()
    co = df['total_count'].tolist()
    # Calculate the count and percentage of True and False values

    counts = df.groupby('Clients')['total_count'].count()
    percentages = per

    # Create a new DataFrame with the counts and percentages
    pie_data = pd.DataFrame({'count': counts, 'percentage': percentages})

    # Reset the index to make 'Clients' a regular column
    pie_data = pie_data.reset_index()
    pie_data['count'] = co
    pie_data['status'] = x['Status']
    # Create the pie chart
    fig = px.pie(pie_data, values='count', names='Clients',color = 'status',hover_name='status', 
                 hover_data=['percentage'], hole=0.7)
    fig.update_traces(textposition='outside', textinfo='label',textfont=dict(size=13))

    figures.append(fig)
    return figures

col = ['Diginews', 'DigiConnect OBD/IVR',
       'DigiConnect Whatsapp promotional', 'DigiConnect SMS',
       'Emailer Campaign (Amity Delhi)', 'Digitrack Only Miss Call',
       'Digitrack SMS/Whatsapp Plugin', 'Digiscan', 'Digiask', 'DigiSampling',
       'Digireach CPI', 'Digireach CPL', 'DigiServices']
column_name = st.sidebar.selectbox('Select Product',col,index = 0)

figures = required_df(df,column_name)
st.header(column_name)
st.plotly_chart(figures[0])
