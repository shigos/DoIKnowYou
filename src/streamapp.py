import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import cv2
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras import models
import os
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
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
        
        model = load_model('../models/inceptionmodel.h5')
        image = load_img(image_data, target_size=(150, 150))
        image = img_to_array(image)
        print(image)
        image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
        image = preprocess_input(image) #I think this is where we put the preprocess input we used for the test images
        yhat = model.predict(image)
        return yhat
        # label = decode_predictions(yhat)
    # return highest probability 
        
        # size = (150,150)    
        # image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        # image = np.asarray(image)
        # img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # img_resize = (cv2.resize(img, dsize=(150, 150),    interpolation=cv2.INTER_CUBIC))/255.
        
        # img_reshape = img_resize[np.newaxis,...]
    
        # prediction = model.predict(img_reshape)
        
        # return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image)
    data = file.read()
    prediction = import_and_predict(data)
    
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
