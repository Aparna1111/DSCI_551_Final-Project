import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO, StringIO
from PIL.ExifTags import TAGS

def app():
	df1 = pd.read_csv('Recommendations_Pantry.csv')

	st.title("Recommendation based on category: Pantry")
	st.subheader("Upload an image and we will recommend what other pantry items you might like")

	# Code to read a single file 
	pantry_file = st.file_uploader("Choose a file", type = ['jpg', 'png', 'jpeg'])
	pantry_show_file = st.empty()


	# IMAGE CLASSIFIER MODEL IS LOADED FOR PREDICTION
	# with open('model.pkl' , 'rb') as f:
	# 	lr = pickle.load(f)

	# 	img = cv2.imread(bakery_file)
	# 	img = cv2.resize(img,(150,150))

	# 	img = np.reshape(img,[-1,150,150,3])
	# 	x = lr.predict(img)
	if pantry_file is not None:
		#content = file.getvalue()
		text=pantry_file.name
		pantry_show_file.image(pantry_file)
		st.write("**Image metadata:**")
		pantry_file_details = {	
      	"FileName": pantry_file.name,
      	"FileType": pantry_file.type,
      	"FileSize": pantry_file.size
   		}
		st.write(pantry_file_details)
		pantry_image = Image.open(pantry_file)
		pantry_exifdata = pantry_image.getexif()
		for tagid in pantry_exifdata:
			tagname = TAGS.get(tagid, tagid)
			value = pantry_exifdata.get(tagid)
			st.write(f"{tagname:25}: {value}")
		if text.startswith(("FLOUR","SUGAR","RICE","SPICES","OIL")):
		# if x == ["flour","sugar","rice","spices","oil"]:
			st.write('**Recommendations:**')
			# recommendation = {
        	# 	"1": "cereal",
			# 	"2": "coffee",
			# 	"3": "cream",
			# 	"4": "packaged cheese",
			# 	"5": "tea"

      		# }
			# st.write(recommendation)
			st.table(df1)
		else:
			st.write("No recommendations")

	else:	
		pantry_show_file.info("Please upload a file of type: " + ", ".join(["jpeg", "png", "jpg"]))

	# Code for Saving uploaded Image to Test Folder
	# with open(os.path.join("Test",pantry_file.name),"wb") as f:
	# 	f.write((pantry_file).getbuffer())
	# 	st.success("File Saved")