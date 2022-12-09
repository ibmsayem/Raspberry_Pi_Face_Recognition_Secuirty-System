# Raspberry_Pi-based_Face_Recognition_Secuirty-System
This project is aimed to design a portable security camera by utilizing simple image processing. The proposed system is highly suitable for Security Camera application with Face Recognition feature and Email notifications.The hardware components utilized in this system is **Raspberry Pi 3 Model B**, and **Raspberry Pi camera Sensor**. A 16GB of meomory is used which comes with **Raspbian OS**. It is developed with _**Pyhton 3.**_ 
The objective of the system is to provide access to authroized people in a restricted area.


It has total three steps: **1) Data collection, 2) Model training, and 3) Model deployment**

## Worflow of the the System:
### Data Collction
The data collection process starts with taking 30 images of different people who are authorized to enter a secured locations. Agfter running the **_face_datset.py_** the program starts the camera and start taking pictures from the video and save it to the local directory. Each images has unique Id. In order to capture the face from the video we used **_haarcascade_frontalface_** classifier.

### Model Training
After the data collection we train the images and during training **_LBPH Face Recognizer_** is used and save the train data in an **.xml** file. 

### Model Deployment
After the training process the model is deployed, where it is give access to the people in a restricted area only to the people with whom the model is trained. When an unknown people come in front of camera it takes the images of that person and send an email to the administration and as a security alert. Simple Mail Transfer Protocol (SMTP) is used to send the Email. 

[Integrating Face Recognition Security System with IoT]([https://pages.github.com/](https://ieeexplore.ieee.org/abstract/document/8613996)).

Biblatex entry:

@inproceedings{sayem2018integrating,
  title={Integrating face recognition security system with the internet of things},
  author={Sayem, Ibrahim Mohammad and Chowdhury, Mohammad Sanaullah},
  booktitle={2018 International Conference on Machine Learning and Data Engineering (iCMLDE)},
  pages={14--18},
  year={2018},
  organization={IEEE}
}

