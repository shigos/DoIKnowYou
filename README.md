
# Face to Face
1. [Description of Project](https://github.com/shigos/DoIKnowYou/blob/main/README.md#description-of-project) 
2. [Data Description](https://github.com/shigos/DoIKnowYou/blob/main/README.md#data-description)
3. [EDA](https://github.com/shigos/DoIKnowYou/blob/main/README.md#eda)
4. [Data Cleaning](https://github.com/shigos/DoIKnowYou/blob/main/README.md#data-cleaning)
5. [Models]()
6. [Conclusion]()

 ## Description of Project
Facial recognition has been adopted as one of the most common means of biometric identification in our every day lives. From banking authentication, photo labeling, to security and healthcare, there can be many applications for facial recognition technology. The goal of this project is to see if it is possible to implement a transfer learning model for an accurate celebrity prediction depsite having limited data. 

## Data Description
 The FaceScrub dataset was created in 2015 containing 100,000 images of 530 different celebrities. The dataset is compiled using a txt file format which contains links with a downloading script. Due to the age of the data set, the final download only yielded a total of 30,000 photos.


## EDA
  The subset used for modeling purposes contains approximately 1200 photos with an average of 80 per class. Below are the 26 classes along with the number of images in each class. 
  
  
  
Aaron_Eckhart 92,
Alan_Rickman 93,
Alice_Krige 33,
Bernie_Mac 51,
Bill_Cosby 63,
Bradley_Cooper 98,
Bruce_Willis 102,
Chris_Evans 59,
Courteney_Cox 125,
Danny_Glover 62,
Denzel_Washington 73,
Don_Cheadle 77,
Eileen_Davidson 81,
Ellen_DeGeneres 77,
Farrah_Fawcett 76,
Jennette_McCurdy 105,
Jet_Li 83,
Jim_Carrey 89,
Jimmy_Fallon 65,
Matt_Damon 118,
Nicolas_Cage 86,
Nicole_Eggert 63,
Patrick_Swayze 81,
Robert_Downey_Jr. 67,
Samuel_L._Jackson 72,
Selena_Gomez 85

The celebrity class containing the most images is Courtney Cox with 125, while the celebrity class with the lowest number of images is Alice Krige with 33
Here are two sample images that were fed into the models of the respective classes. 



![Courteney_Cox_35355_16220](https://user-images.githubusercontent.com/76585249/132271101-043c2685-bf25-48ee-8fc5-2d445753b153.jpeg)



![Alice_Krige_89438_40707](https://user-images.githubusercontent.com/76585249/132271110-ec2be154-00cb-451f-919e-723f572c94b6.jpeg)


A distribution of the counts of images are shown in the graph below.

![eda](https://user-images.githubusercontent.com/76585249/132273176-7ffc12e5-14a7-4400-9b6c-846658a62a88.png)

During my exploratory data analysis of the images provided, it seems that there contained images that seemed to be morphed and could possibly throw off the model's prediction. Due to the large amounts of photos within the dataset, there is no possible way to find all morphed images. 


![sameul l jackson](https://user-images.githubusercontent.com/76585249/132273589-8b247706-4959-42aa-8c6b-5761b517ea27.png)


Image above was found in the Samuel L. Jackson file but seems to be a morphed image of both Samuel L. Jackson and Bruce Willis.


## Data Cleaning

  The images prior to cleaning come in different sizes capture the subject while the images that were fed into the model were normalized and reshaped to be consistent throughout the training data.
  
Examples below show images prior to normalization and resizing


![rdj](https://user-images.githubusercontent.com/76585249/132273292-0a95c55a-0724-4838-ae7b-fc1e00bc86a1.png)


![jb](https://user-images.githubusercontent.com/76585249/132273296-1c9186aa-1fdc-4d61-a07c-4412afdac387.png)


Example images below show photos post nomalization and resizing, the way they are fed into the model.


![sal](https://user-images.githubusercontent.com/76585249/132273360-1dfcfb30-1be5-4d72-b25f-9c8ab770796e.jpg)

![cr](https://user-images.githubusercontent.com/76585249/132273349-63f798d2-f8ca-456d-9518-c61d2197a417.jpg)

  
  
  
## Model Training
  A baseline was created using the celebrity(class) with the most images. With 125 images, our baseline is set to be about a 6% accuracy.
