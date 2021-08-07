import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def data_pross(path):

    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    test_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = train_datagen.flow_from_directory(
        path,
        target_size=(150, 150),
        color_mode='grayscale',
        batch_size=10,
        class_mode='categorical')
    validation_generator = test_datagen.flow_from_directory(
        path,
        target_size=(150, 150),
        color_mode='grayscale',
        batch_size=10,
        class_mode='categorical')
    





