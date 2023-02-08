# from matplotlib import pyplot as plt
# from collections import Counter

import plotly.express as px
import streamlit as st
import pandas as pd

datapath = 'jan23data/'
aadata = 'scores_aa_2022.csv'
ngdata = 'scores_nextgen_2022.csv'

# interpretations = pd.read_csv('scores_interpretations.csv')

# print(interpretations)

monAA = pd.read_csv(datapath+aadata,header=[0,1])[['date','interpretation']].droplevel(0,axis=1)
monNG = pd.read_csv(datapath+ngdata,header=[0,1])[['date','interpretation']].droplevel(0,axis=1)

# monAA = pd.read_csv('data/monthly_scores_AA_chirps.csv',header=[0,1])[['date','interpretation']].droplevel(0,axis=1)
# monNG = pd.read_csv('data/monthly_scores_nextgen_chirps.csv',header=[0,1])[['date','interpretation']].droplevel(0,axis=1)

monAA['source'] = 'Años Análogos'
monNG['source'] = 'NextGen'

mondf = pd.concat([monAA,monNG],ignore_index=True)

# mondf = mondf[((mondf['month']>=5) & (mondf['month']<=11))]
# mondf = mondf[~((mondf['month']>=5) & (mondf['month']<=11))]


# HRdf = pd.DataFrame({'AA':monAA['HR'].values,'NG':monNG['HR'].values})

hr = px.histogram(mondf,'HR',color='source',barmode='group')
hss = px.histogram(mondf,'HSS',color='source',barmode='group')
afc = px.histogram(mondf,'2AFC',color='source',barmode='group')
leps = px.histogram(mondf,'LEPS',color='source',barmode='group')

# print('\nAA:\n')
# print(monAA['HR'].value_counts())
# print('\nNG:\n')
# print(monNG['HR'].value_counts())

hr_df = monAA['HR'].value_counts()

# hr_pie = px.pie(hr_df,names='Score',values='count')

print(hr_df)
print(type(hr_df))
print(hr_df.to_frame(name='count'))

for row in hr_df:
    print(row)

########################################################################################################################################
# FrontEnd
st.set_page_config(layout="wide")
st.title('Histogramas de conteo de puntuaciones')




# with cols[0]:
#     year = st.slider('Year',2019,2022)


# hr = px.histogram(mondf[mondf['year']==year],'HR',category_orders=dict(HR = interpretations['HR'].values),color='source',barmode='group')
# hss = px.histogram(mondf[mondf['year']==year],'HSS',category_orders=dict(HR = interpretations['HSS'].values),color='source',barmode='group')
# afc = px.histogram(mondf[mondf['year']==year],'2AFC',category_orders=dict(HR = interpretations['2AFC'].values),color='source',barmode='group')

#####################################
st.subheader('HR')
cols = st.columns(2)

with cols[0]:
    st.plotly_chart(hr)
# with cols[1]:
    # st.plotly_chart(hr_pie)
#####################################
#####################################
st.subheader('HSS')
cols = st.columns(2)  

with cols[0]:
    st.plotly_chart(hss)
with cols[1]:
    st.plotly_chart(hss)
#####################################
#####################################
st.subheader('2AFC')
cols = st.columns(2)  

with cols[0]:
    st.plotly_chart(afc)
with cols[1]:
    st.plotly_chart(afc)
#####################################
st.subheader('LEPS')
cols = st.columns(2)

with cols[0]:
    st.plotly_chart(leps)
with cols[1]:
    st.plotly_chart(leps)

