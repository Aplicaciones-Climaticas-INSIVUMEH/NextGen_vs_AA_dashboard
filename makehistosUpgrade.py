# from matplotlib import pyplot as plt
# from collections import Counter

import plotly.express as px
import streamlit as st
import pandas as pd
import datetime as dt

datapath = 'jan23data/'
aadata = 'climaest_scores_aa_2021-2022.csv'
ngdata = 'climaest_scores_nextgen_2021-2022.csv'

metrics = ['HR','HSS','2AFC','LEPS']

years = [2021,2022,2023]
months = ['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic']
months_to_number = {'ene':1,'feb':2,'mar':3,'abr':4,'may':5,'jun':6,'jul':7,'ago':8,'sep':9,'oct':10,'nov':11,'dic':12}

monAA_original = pd.read_csv(datapath+aadata,header=[0,1])[['date','interpretation']].droplevel(0,axis=1)
monNG_original = pd.read_csv(datapath+ngdata,header=[0,1])[['date','interpretation']].droplevel(0,axis=1)
scoreinterp = pd.read_csv('scores_interpretations.csv')

GrPi = ['#c77de0','#ddf458']
Pis = ['#c77de0','#8053db','#2d24cc','#120d72']
Grs = ['#ddf458','#7da81f','#246d10','#044c2d']

def get_ranges(selected_years_input,selected_months_input,monAA_input,monNG_input):

    # print(selected_years_input)

    monAA = monAA_input[(monAA_input['year'].isin(selected_years_input) & monAA_input['month'].isin(selected_months_input))].copy()
    # monAA = monAA_input[monAA_input['month'].isin(selected_months_input)].copy()

    monNG = monNG_input[(monNG_input['year'].isin(selected_years_input) & monNG_input['month'].isin(selected_months_input))].copy()
    # monNG = monNG_input[monNG_input['month'].isin(selected_months_input)].copy()

    # print(monAA)
    # print(monNG)

    # monAA = monAA_original
    # monNG = monNG_original

    monAA['source'] = 'Años Análogos'
    monNG['source'] = 'NextGen'

    mondf = pd.concat([monAA,monNG],ignore_index=True)

    # print(mondf)

    return monAA, monNG, mondf



def build_charts(monAA_input,monNG_input,mondf_input):
    barcharts = dict()
    aapiecharts = dict()
    ngpiecharts = dict()

    for metric in metrics:
        catords = {metric:scoreinterp[metric].to_list()}
        # catordspie = {'':scoreinterp[metric].to_list()}

        barcharts[metric] = px.histogram(mondf_input,metric,color='source',barmode='group',color_discrete_sequence=GrPi,category_orders=catords)#px.colors.diverging.Temps)

        metric_aadata = monAA_input[metric].value_counts().to_frame(name='count')
        metric_aadata[metric] = metric_aadata.index
        aapiecharts[metric] = px.pie(metric_aadata,names=metric,values='count',color_discrete_sequence=Pis,category_orders=catords,hole=0.4)#px.colors.sequential.Plotly3)
        
        aapiecharts[metric].update_layout(legend=dict(
        yanchor="top",
        y=0.01,
        xanchor="left",
        x=0.01
        ),title = {
            'text': "AA",
            'y':0.5, # new
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom' # new
            })

        metric_ngdata = monNG_input[metric].value_counts().to_frame(name='count')
        metric_ngdata[metric] = metric_ngdata.index
        ngpiecharts[metric] = px.pie(metric_ngdata,names=metric,values='count',color_discrete_sequence=Grs,category_orders=catords,hole=0.4)#px.colors.sequential.Aggrnyl)

        ngpiecharts[metric].update_layout(legend=dict(
        yanchor="top",
        y=0.01,
        xanchor="left",
        x=0.01
        ),title = {
            'text': "NG",
            'y':0.5, # new
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'bottom' # new
            })
        
    return barcharts,aapiecharts,ngpiecharts

def build_page(selected_years_input,selected_months_key_input):
    selected_months = []
    for month in selected_months_key_input:
        selected_months.append(months_to_number[month])

    # print(selected_years_input)

    monAA, monNG, mondf = get_ranges(selected_years_input,selected_months,monAA_original,monNG_original)
    barcharts, aapiecharts, ngpiecharts = build_charts(monAA,monNG,mondf)

    tabs = st.tabs(metrics)

    for metric,tab in zip(metrics,tabs):
    #####################################
        with tab:
            # st.subheader(metric)
            
            cols = st.columns((5,3,3))
            with cols[0]:
                st.plotly_chart(barcharts[metric],use_container_width=True)
            with cols[1]:
                # st.text("AA")
                st.plotly_chart(aapiecharts[metric],use_container_width=True)
            with cols[2]:
                # st.text("NG")
                st.plotly_chart(ngpiecharts[metric],use_container_width=True)
            
    #####################################


########################################################################################################################################
# FrontEnd
st.set_page_config(layout="wide")
st.title('Evaluación de Métricas')

selected_years = years
selected_months_key = months


with st.expander('Filtros:'):
    selected_years = st.multiselect('Años:',years,years)
    selected_months_key = st.multiselect('Meses:',months,months)

build_page(selected_years,selected_months_key)






