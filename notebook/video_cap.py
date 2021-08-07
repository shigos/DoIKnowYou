model = models.load_model('gender.h5')
model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))
video = cv2.VideoCapture(0)

while True:
        _, frame = video.read()

        #Convert the captured frame into RGB
        im = Image.fromarray(frame, 'RGB')

        #Resizing into dimensions you used while training
        im = im.resize((109,82))
        img_array = np.array(im)

        #Expand dimensions to match the 4D Tensor shape.
        img_array = np.expand_dims(img_array, axis=0)

        #Calling the predict function using keras
        prediction = model.predict(img_array)#[0][0]
        print(prediction)
        #Customize this part to your liking...
        if(prediction == 1 or prediction == 0):
            print("No Human")
        elif(prediction < 0.5 and prediction != 0):
            print("Female")
        elif(prediction > 0.5 and prediction != 1):
            print("Male")

        cv2.imshow("Prediction", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()