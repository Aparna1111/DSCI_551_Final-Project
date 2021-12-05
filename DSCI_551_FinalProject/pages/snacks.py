import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO, StringIO
from PIL.ExifTags import TAGS

def app():
	df1 = pd.read_csv('Recommendations_Snacks.csv')
	st.title("Product recommendation based on category: Snacks")
	st.subheader("Upload an image and we will recommend what other snacks you might like")

 	# Code to read a single file 
	file = st.file_uploader("Choose a file", type = ['jpg', 'png', 'jpeg'])
	show_file = st.empty()

	# IMAGE CLASSIFIER MODEL IS LOADED FOR PREDICTION
	# with open('model.pkl' , 'rb') as f:
	# 	lr = pickle.load(f)

	# 	img = cv2.imread(bakery_file)
	# 	img = cv2.resize(img,(150,150))

	# 	img = np.reshape(img,[-1,150,150,3])
	# 	x = lr.predict(img)
	if file is not None:
		#content = file.getvalue()
		text = file.name
		show_file.image(file)
		st.write("**Image metadata:**")
		file_details = {	
      	"FileName": file.name,
      	"FileType": file.type,
      	"FileSize": file.size
   		}
		st.write(file_details)
		image = Image.open(file)
		exifdata = image.getexif()
		for tagid in exifdata:
			tagname = TAGS.get(tagid, tagid)
			value = exifdata.get(tagid)
			st.write(f"{tagname:25}: {value}")
		if text.startswith(("CHIPS","CANDY","NUTS")):
		# if x == ["chips","candy","nuts"]:
			st.write('**Recommendations:**')
			# recommendation = {
        	# 	"1": "candy chocolate",
			# 	"2": "canned fruit applesauce",
			# 	"3": "condiments",
			# 	"4": "crackers",
			# 	"5": "cookies"

      		# }
			# st.write(recommendation)
			st.table(df1)
		else:
			st.write("No recommendations")

	else:	
		show_file.info("Please upload a file of type: " + ", ".join(["jpeg", "png", "jpg"]))

	# Code for Saving uploaded Image to Test Folder
	# with open(os.path.join("Test",file.name),"wb") as f:
	# 	f.write((file).getbuffer())
	# 	st.success("File Saved")
