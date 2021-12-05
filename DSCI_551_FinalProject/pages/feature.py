import streamlit as st
import pandas as pd

def app():
	st.subheader("Features Extracted from Raw Data")
    st.write("The features extracted from the raw data along with it's cluster number are visible in the csv's below")
	df_bakery = pd.read_csv('Bakery.csv')
    df_beverages = pd.read_csv('Beverages.csv')
    df_pantry = pd.read_csv('pantry.csv')
    df_snacks = pd.read_csv('Snacks.csv')

	option = st.selectbox('Select the csv file to explore for the specific department',('Select CSV','Bakery','Beverages','Pantry', 'Snacks'))

	if option=="Bakery":
		st.table(df_bakery)

	elif option=="Beverages":
		st.table(df_beverages)

	elif option=="Pantry":
		st.table(df_pantry)

	elif option=="Snacks":
		st.table(df_snacks)
