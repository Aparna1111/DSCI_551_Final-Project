import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO, StringIO
from PIL.ExifTags import TAGS

def app():
	df1 = pd.read_csv('Recommendations_Beverages.csv')



	st.title("Recommendation based on category: Beverages")
	st.subheader("UUpload an image and we will recommend what other beverages you might like")

	# Code to read a single file 
	bev_file = st.file_uploader("Choose a file", type = ['jpg', 'png', 'jpeg'])
	bev_show_file = st.empty()

	# IMAGE CLASSIFIER MODEL IS LOADED FOR PREDICTION
	# with open('model.pkl' , 'rb') as f:
	# 	lr = pickle.load(f)

	# 	img = cv2.imread(bakery_file)
	# 	img = cv2.resize(img,(150,150))

	# 	img = np.reshape(img,[-1,150,150,3])
	# 	x = lr.predict(img)
	if bev_file is not None:
		#content = file.getvalue()
		text = bev_file.name
		bev_show_file.image(bev_file)
		st.write("**Image metadata:**")
		bev_file_details = {	
      	"FileName": bev_file.name,
      	"FileType": bev_file.type,
      	"FileSize": bev_file.size
   		}
		st.write(bev_file_details)
		bev_image = Image.open(bev_file)
		bev_exifdata = bev_image.getexif()
		for tagid in bev_exifdata:
			tagname = TAGS.get(tagid, tagid)
			value = bev_exifdata.get(tagid)
			st.write(f"{tagname:25}: {value}")
		if text.startswith(("MILK","SODA","WATER","TEA","COFFEE","JUICE")):
		# if x == ["milk","soda","water","tea","coffee","juice"]:
			st.write('**Recommendations:**')
			
			st.table(df1)
		else:
			st.write("No recommendations")

	else:	
		bev_show_file.info("Please upload a file of type: " + ", ".join(["jpeg", "png", "jpg"]))


	# Code for Saving uploaded Image to Test Folder
	# with open(os.path.join("Test",bev_file.name),"wb") as f:
	# 	f.write((bev_file).getbuffer())
	# 	st.success("File Saved")


