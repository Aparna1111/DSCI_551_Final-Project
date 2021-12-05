import os
import streamlit as st
import numpy as np
from PIL import  Image

from multipage import MultiPage
from pages import home, snacks, bakery, beverages, pantry, data, rawdata, features

# Create an instance of the app 
app = MultiPage()

st.title("Grocery Recommendation System")
#st.subheader("Upload an image for analysis and recommendation or")

# Add all your application here
app.add_page("Home Page", home.app)
app.add_page("Snacks Recommendation", snacks.app)
app.add_page("Bakery Recommendation", bakery.app)
app.add_page("Beverages Recommendation", beverages.app)
app.add_page("Pantry Recommendation",pantry.app)
app.add_page("Explore Raw Data", data.app)
app.add_page("Explore Metadata of Dataset", rawdata.app)
app.add_page("Explore Extracted Features", features.app)
#app.add_page("Y-Parameter Optimization",redundant.app)

# The main app
app.run()