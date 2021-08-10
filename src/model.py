import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img,img_to_array
from tensorflow.keras.optimizers import Adam
from sklearn import metrics
import numpy as np
import os 
import cv2
import sys
from argparse import ArgumentParser


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
class Model:



    def __init__(self,args):
        self.model = keras.models.load_model('../models/inceptionmodel.h5')
        self.args = args


    def load_model(self):
        return self.model


    def load_image(self):
        
        my_image = load_img(self.args.test_path, color_mode = 'rgb' ,target_size=(150, 150))
        my_image = img_to_array(my_image)/255
        my_image = my_image.reshape((1, my_image.shape[0], my_image.shape[1], my_image.shape[2]))

        return my_image

   

def main(args):
    lst =['Aaron_Eckhart',
 'Alan_Rickman',
 'Alice_Krige',
 'Bernie_Mac',
 'Bill_Cosby',
 'Bradley_Cooper',
 'Bruce_Willis',
 'Chris_Evans',
 'Courteney_Cox',
 'Danny_Glover',
 'Denzel_Washington',
 'Don_Cheadle',
 'Eileen_Davidson',
 'Ellen_DeGeneres',
 'Farrah_Fawcett',
 'Jennette_McCurdy',
 'Jet_Li',
 'Jim_Carrey',
 'Jimmy_Fallon',
 'Matt_Damon',
 'Nicolas_Cage',
 'Nicole_Eggert',
 'Patrick_Swayze',
 'Robert_Downey_Jr.',
 'Samuel_L._Jackson',
 'Selena_Gomez']
    my_model = Model(args)
    test_image = my_model.load_image()
    regressor = my_model.model
    ret=regressor.predict(test_image)
    for i, name  in enumerate(lst):
        if i == (np.argmax(ret[0])):
            print(name)
   

    return regressor.predict(test_image)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('--test_path',required = True, type = str, help='img file path to load into model')

    args = parser.parse_args()
    main(args)