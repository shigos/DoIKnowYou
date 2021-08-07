import tensorflow as tf
from tensorflow import keras



def fit_model(train_generator,validation_generator):
    history = model.fit(train_generator,
                    epochs=300,
                    validation_data = validation_generator, 
                    callbacks = [es,mc])
    score = model.evaluate(validation_generator, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1]) 
