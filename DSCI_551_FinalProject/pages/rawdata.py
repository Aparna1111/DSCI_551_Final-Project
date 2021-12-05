import streamlit as st
import pandas as pd
import csv

def app():
	st.subheader("Explore the metadata of the dataset used")
	df1 = pd.read_csv('aisles.csv')
	df2 = pd.read_csv('departments.csv')
	df3 = pd.read_csv('products.csv')
	df4 = pd.read_csv('orders.csv')
	df5 = pd.read_csv('train.csv')
	df6 = pd.read_csv('prior.csv')

	option = st.selectbox('Select the csv file to explore',('Select CSV','Aisles','Departments','Products', 'Orders', 'Trained Dataset', 'Prior Orders'))

	if option=="Aisles":
		st.subheader("**Metadata:**")
		total_cols=len(df1.axes[1])
		total_rows=len(df1.axes[0])
		st.write("**Number of attributes:**" + str(total_cols))
		st.write("**Number of rows:**" + str(total_rows))
		st.write("**Attribute Names:**")
		for col_name in df1.columns:
			st.write(col_name)


	elif option=="Departments":
		st.subheader("**Metadata:**")
		total_cols=len(df2.axes[1])
		total_rows=len(df2.axes[0])
		st.write("**Number of attributes:**" + str(total_cols))
		st.write("**Number of rows:**" + str(total_rows))
		st.write("**Attribute Names:**")
		for col_name in df2.columns:
			st.write(col_name)

	elif option=="Products":
		st.subheader("**Metadata:**")
		total_cols=len(df3.axes[1])
		total_rows=len(df3.axes[0])
		st.write("**Number of attributes:**" + str(total_cols))
		st.write("**Number of rows:**" + str(total_rows))
		st.write("**Attribute Names:**")
		for col_name in df3.columns:
			st.write(col_name)

	elif option=="Orders":
		st.subheader("**Metadata:**")
		total_cols=len(df4.axes[1])
		total_rows=len(df4.axes[0])
		st.write("**Number of attributes:**" + str(total_cols))
		st.write("**Number of rows:**" + str(total_rows))
		st.write("**Attribute Names:**")
		for col_name in df4.columns:
			st.write(col_name)

	elif option=="Trained Dataset":
		st.subheader("**Metadata:**")
		total_cols=len(df5.axes[1])
		total_rows=len(df5.axes[0])
		st.write("*Number of attributes:**" + str(total_cols))
		st.write("**Number of rows:**" + str(total_rows))
		st.write("**Attribute Names:**")
		for col_name in df5.columns:
			st.write(col_name)

	elif option=="Prior Orders":
		st.subheader("**Metadata:**")
		total_cols=len(df6.axes[1])
		total_rows=len(df6.axes[0])
		st.write("**Number of attributes:**" + str(total_cols))
		st.write("**Number of rows:**" + str(total_rows))
		st.write("**Attribute Names:**")
		for col_name in df6.columns:
			st.write(col_name)