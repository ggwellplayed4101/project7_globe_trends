import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Exploring Correlations Between Different National Metrics")

x_axis = st.selectbox("Select the data for the X-axis", 
             ("Happiness","GDP","Social Support",
              "Life Expectancy","Freedom to make life choices",
              "Generosity","Corruption"))

y_axis = st.selectbox("Select the data for the Y-axis", 
             ("Happiness","GDP","Social Support",
              "Life Expectancy","Freedom to make life choices",
              "Generosity","Corruption"))

def get_data(topic):
    df = pd.read_csv("happy.csv")
    data_dict = {
        "Happiness": "happiness",
        "GDP": "gdp",
        "Social Support": "social_support",
        "Life Expectancy": "life_expectancy",
        "Freedom to make life choices": "freedom_to_make_life_choices",
        "Generosity": "generosity",
        "Corruption": "corruption"
    }
    data = df[data_dict[topic]]
    return(data)

x_data = get_data(x_axis)
y_data = get_data(y_axis)

graph = px.scatter(x=x_data, y=y_data,
                   labels={"x": x_axis, "y": y_axis})
st.plotly_chart(graph)