import streamlit as st
import pandas as pd

def app():
	st.subheader("Explore the raw data used in the application")
	#st.write("Select the csv file to explore") 
	df1 = pd.read_csv('aisles.csv')
	df2 = pd.read_csv('departments.csv')
	df3 = pd.read_csv('products.csv')
	df4 = pd.read_csv('orders.csv')
	df5 = pd.read_csv('train.csv')
	df6 = pd.read_csv('prior.csv')

	option = st.selectbox('Select the csv file to explore',('Select CSV','Aisles','Departments','Products', 'Orders', 'Trained Dataset', 'Prior Orders'))

	if option=="Aisles":
		st.table(df1)

	elif option=="Departments":
		st.table(df2)

	elif option=="Products":
		st.table(df3)

	elif option=="Orders":
		st.table(df4)

	elif option=="Trained Dataset":
		st.table(df5)

	elif option=="Prior Orders":
		st.table(df6)
