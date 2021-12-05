import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO, StringIO
from PIL.ExifTags import TAGS

def app():
	st.subheader("We provide the following features in this application. Please find the same in left side navigation bar")
	st.write("1. Product Recommendation based on category: Snacks")
	st.write("2. Product Recommendation based on category: Bakery")
	st.write("3. Product Recommendation based on category: Beverages")
	st.write("4. Product Recommendation based on category: Pantry")
	st.write("5. Extract metadata from the uploaded images")
	st.write("6. Explore the dataset used in the model")
	st.write("7. Extract metadata from the dataset")