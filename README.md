# Face to Face
1. [Description of Project](https://github.com/shigos/DoIKnowYou/blob/main/README.md#description-of-project) 
2. [Data Description](https://github.com/shigos/DoIKnowYou/blob/main/README.md#data-description)
3. [Cleaning/Notebooks]()
4. [EDA]()
5. [Models]()
6. [Conclusion]()

 ### Description of Project
Facial recognition has been adopted as one of the most common means of biometric identification in our every day lives. From banking authentication, photo labeling, to security and healthcare, there can be many applications for facial recognition technology. The goal of this project is to see if it is possible to implement a transfer learning model for an accurate celebrity prediction depsite having limited data. 

### Data Description
 The FaceScrub dataset was created in 2015 containing 100,000 images of 530 different celebrities. The dataset is compiled using a txt file format which contains links with a downloading script. Due to the age of the data set, the final download only yielded a total of 30,000 photos.
The subset used for modeling purposes contains approximately 1200 photos with an average of 80 per class. The celebrities(classes) in the model contains 'Aaron_Eckhart','Alan_Rickman','Alice_Krige','Bernie_Mac','Bill_Cosby','Bradley_Cooper','Bruce_Willis','Chris_Evans','Courteney_Cox','Danny_Glover','Denzel_Washington','Don_Cheadle','Eileen_Davidson','Ellen_DeGeneres','Farrah_Fawcett','Jennette_McCurdy','Jet_Li','Jim_Carrey','Jimmy_Fallon','Matt_Damon','Nicolas_Cage','Nicole_Eggert','Patrick_Swayze','Robert_Downey_Jr.','Samuel_L._Jackson','Selena_Gomez'


### EDA
 
### Model Training
  A baseline was created using the celebrity(class) with the most images. With 1-- images, our baseline is set to be about a 6% accuracy.
