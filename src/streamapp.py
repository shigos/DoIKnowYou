import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
import sklearn
from tensorflow.keras.models import load_model



st.write("""
         # Celebrity Classification  
         """
         )
         
st.write("Load image for celebrity classification prediction")

file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

def import_and_predict(image_data):
        
        model = tf.keras.models.load_model('/Users/winsometang/dsi_galvanize/capstone/DoIKnowYou/models/inceptionmodel.h5')
        
        image = img_to_array(image_data)/255
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        
        image = model.predict(image)
        return image
        

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image)
    feed = Image.open(file).convert('RGB')
    feed = feed.resize((150,150))
    prediction = import_and_predict(feed)
    
    if np.argmax(prediction) == 0:
        st.write("Aaron_Eckhart")
    elif np.argmax(prediction) == 1:
        st.write("Alan_Rickman")
    elif np.argmax(prediction) == 2:
        st.write("Alice_Krige")
    elif np.argmax(prediction) == 3:
        st.write("Bernie_Mac")
    elif np.argmax(prediction) == 4:
        st.write("Bill_Cosby")
    elif np.argmax(prediction) == 5:
        st.write("Bradley_Cooper")
    elif np.argmax(prediction) == 6:
        st.write("Bruce_Willis")
    elif np.argmax(prediction) == 7:
        st.write("Chris_Evans")
    elif np.argmax(prediction) == 8:
        st.write("Courteney_Cox")
    elif np.argmax(prediction) == 9:
        st.write("Danny_Glover")
    elif np.argmax(prediction) == 10:
        st.write("Denzel_Washington")
    elif np.argmax(prediction) == 11:
        st.write("Don_Cheadle")
    elif np.argmax(prediction) == 12:
        st.write("Eileen_Davidson")
    elif np.argmax(prediction) == 13:
        st.write("Ellen_DeGeneres")
    elif np.argmax(prediction) == 14:
        st.write("Farrah_Fawcett")
    elif np.argmax(prediction) == 15:
        st.write("Jennette_McCurdy")
    elif np.argmax(prediction) == 16:
        st.write("Jet_Li")
    elif np.argmax(prediction) == 17:
        st.write("Jim_Carrey")
    elif np.argmax(prediction) == 18:
        st.write("Jimmy_Fallon")
    elif np.argmax(prediction) == 19:
        st.write("Matt_Damon")
    elif np.argmax(prediction) == 20:
        st.write("Nicolas_Cage")
    elif np.argmax(prediction) == 21:
        st.write("Nicole_Eggert")
    elif np.argmax(prediction) == 22:
        st.write("Patrick_Swayze")
    elif np.argmax(prediction) == 23:
        st.write("Robert_Downey_Jr.")
    elif np.argmax(prediction) == 24:
        st.write("Samuel_L._Jackson")
    else: 
        # np.argmax(prediction) == 25:
        st.write("Selena_Gomez")


    st.text(f"Probability {prediction})")
    st.write(prediction)
