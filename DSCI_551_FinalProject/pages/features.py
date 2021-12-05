import streamlit as st
import pandas as pd

def app():
	st.subheader("Explore the features extracted")
	#st.write("Select the csv file to explore") 
	df1 = pd.read_csv('Bakery.csv')
	# df1 = df1[df1['department']== 'bakery']
	df1 = df1.drop(['department','order_id', 'aisle_id','department_id',  '_c0'], axis=1)
	df1 = df1.iloc[: , 2:]

	df2 = pd.read_csv('Pantry.csv')
	# df2 = df2[df2['department']== 'pantry']
	df2 = df2.drop(['department','order_id', 'department_id','aisle_id', '_c0'], axis=1)
	df2 = df2.iloc[: , 2:]

	df3 = pd.read_csv('Snacks.csv')
	# df3 = df3[df3['department']== 'snacks']
	df3 = df3.drop(['department','department_id','order_id', 'aisle_id',  '_c0'], axis=1)
	df3 = df3.iloc[: , 2:]

	df4 = pd.read_csv('Beverages.csv')
	# df4 = df4[df4['department']== 'beverages']
	df4 = df4.drop(['department','department_id','order_id', 'aisle_id', '_c0'], axis=1)
	df4 = df4.iloc[: , 2:]

	option = st.selectbox('Select the csv file to explore',('Select CSV','Bakery','Pantry','Snacks', 'Beverages'))

	if option=="Bakery":
		st.table(df1)

	elif option=="Pantry":
		st.table(df2)

	elif option=="Snacks":
		st.table(df3)

	elif option=="Beverages":
		st.table(df4)
