from classify import predict
import streamlit as st
from PIL import Image
import numpy as np

st.write("""
# Simple VGG16 Model Classifier

""")

import streamlit as st
import os

def file_selector(folder_path='./images'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select your Image', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)

# upload_img = st.file_uploader(label='Upload your Image', type=['png', 'jpg'])



if filename:
	img = Image.open(filename)
	st.image(img, caption="Your Image", use_column_width=True)
	st.write("Classifying...")
	label = predict(filename)
	st.write('The image is %s with %.2f%% probabiity' % (label[1], label[2]*100))


# if upload_img is not None:
#     file_bytes = np.asarray(bytearray(upload_img.read()), dtype=np.uint8)
#     opencv_image = cv2.imdecode(file_bytes, 1)