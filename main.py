import streamlit as st
import plotly.express as px

st.title("Exploring Correlations Between Different National Metrics")

x_axis = st.selectbox("Select the data for the X-axis", 
             ("Happiness","GDP","Social Support",
              "Life Expectancy","Freedom to make life choices",
              "Generosity","Corruption"))

y_axis = st.selectbox("Select the data for the Y-axis", 
             ("Happiness","GDP","Social Support",
              "Life Expectancy","Freedom to make life choices",
              "Generosity","Corruption"))

