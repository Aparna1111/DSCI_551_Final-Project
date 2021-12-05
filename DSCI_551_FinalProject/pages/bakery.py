import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO, StringIO
from PIL.ExifTags import TAGS
import cv2
import os
import pickle
import numpy as np
import keras
from keras import backend as K
from keras.utils.np_utils import to_categorical
from keras import layers
from keras.preprocessing.image import save_img
from keras.utils.vis_utils import model_to_dot
from keras.applications.vgg16 import VGG16,preprocess_input
from keras.models import Sequential,Input,Model
from keras.layers import Dense,Flatten,Dropout,Concatenate,GlobalAveragePooling2D,Lambda,ZeroPadding2D
from keras.layers import SeparableConv2D,BatchNormalization,MaxPooling2D,Conv2D
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam,SGD
from keras.utils.vis_utils import plot_model
from keras.callbacks import ModelCheckpoint,EarlyStopping,TensorBoard,CSVLogger,ReduceLROnPlateau,LearningRateScheduler


def app():

	

	df1 = pd.read_csv('Recommendations_Bakery.csv')
	
	st.title("Recommendation based on category: Bakery")
	st.subheader("Upload an image and we will recommend what other bakery items you might like")

	# Code to read a single file 
	bakery_file = st.file_uploader("Choose a file", type = ['jpg', 'png', 'jpeg'])


	# with open('model.pkl' , 'rb') as f:
	# 	lr = pickle.load(f)

	# 	img = cv2.imread(bakery_file)
	# 	img = cv2.resize(img,(150,150))

	# 	img = np.reshape(img,[-1,150,150,3])
	# 	x = lr.predict(img)
	

	bakery_show_file = st.empty()
	
	if bakery_file is not None:
		#content = file.getvalue()
		text = bakery_file.name
		bakery_show_file.image(bakery_file)
		st.write("**Image metadata:**")
		bakery_file_details = {	
      	"FileName": bakery_file.name,
      	"FileType": bakery_file.type,
      	"FileSize": bakery_file.size
   		}
		st.write(bakery_file_details)
		bakery_image = Image.open(bakery_file)
		bakery_exifdata = bakery_image.getexif()
		for tagid in bakery_exifdata:
			tagname = TAGS.get(tagid, tagid)
			value = bakery_exifdata.get(tagid)
			st.write(f"{tagname:25}: {value}")
			
		if text.startswith(("CAKE","JAM","CHOCOLATE")):
			# if x == ["cake","jam","chocolate"]:

				st.write('**Recommendations:**')
			
				st.table(df1)
		else:
			st.write("No recommendations")
	else:	
		bakery_show_file.info("Please upload a file of type: " + ", ".join(["jpeg", "png", "jpg"]))
	
	
	# Code for Saving uploaded Image to Test Folder
	# with open(os.path.join("Test",bakery_file.name),"wb") as f:
	# 	f.write((bakery_file).getbuffer())
	# 	st.success("File Saved")



