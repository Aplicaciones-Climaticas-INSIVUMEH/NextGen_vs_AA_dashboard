import pandas as pd
import streamlit as st
# import plotly.figure_factory as ff
# import plotly.graph_objects as go
import plotly.express as px
import numpy as np

interpretation = pd.read_csv('data/scores_interpretations.csv')
NextGen_AA = pd.read_csv('data/comparison_monthly_forecasts_AA_NextGen_climachirps.csv',header=[0,1])
NextGen_NextGen = pd.read_csv('data/comparison_NextGen_forecasts_monthly_seasonal_climachirps.csv',header=[0,1])

print(interpretation)
print(NextGen_AA)
print(NextGen_NextGen)

data = NextGen_AA[('score_AA','HR')]


# fig = px.bar(NextGen_AA, x=('score_AA','HR'), y=('score_AA','HR'), color="City", barmode="group")
fig = px.histogram(data)


# Plot!
st.plotly_chart(fig, use_container_width=True)