# Indian-Sign-Language
The Projects focuses on providing solution for communication barrier faced by people who are specially abled and use sign languages.


# Introduction

People with visual and hearing impairments find it difficult to communicate with those who do not know sign language. In case they want to communicate, they have to carry additional devices or need an interpreter which makes communication cumbersome. In many situations, the process becomes very inefficient and the user becomes very dependent.
 A computer vision based interactive mobile application which recognizes sign language through hand gestures, movement, orientation of fingers using image processing and converts it into text and speech. 
The application will use a deep learning model for the classification of images into words, sentences and alphabets. This predicted text will then be displayed on the screen of the user's  smartphone. 

![Output sample](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/results/gifgifgifgif.gif)
![Output sample](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/results/ezgif.com-video-to-gif.gif)

# Installation Guide
Here are the steps and procedures you need to follow in order to execute our project as given in [Intallation guide](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/Installation%20Guide.docx)

Step 1: Download the source code and make sure that all the files are contained in a single directory “sign_language” (only an example the directory can have any other name)

Step 2: Download the test data already provided with the file name test_data and keep it in the same directory (sign_language)

Step 3: Go to the directory sign language

Step 4: Install all the required dependencies by running requirements.txt
The following command shall be used on the terminal (preferred os Linux)
```
chmod +x dependencies.sh
./dependencies.sh
```

Step 5: We have converted our text library into a voice using Python Text To Speech | pyttsx module, hence it is important that
it is installed in the graphical interface. You can proceed with the same using the following command.
```
pip3 install pyttsx3
```
Step 6: Run the major source file named 'project.py' it contains access to the source code for the various model used in the project
```
python3 project.py
```

SOME IMPORTANT NOTES FOR RUNNING (INTERFACE 1)
1. A sufficient amount of light is needed. Not too much not too less. And preferably avoid using in sunlight,
 as its yellow light will make everything look skin color alike.
2. For best results, use a plain surface.
3. Your hand must be inside the rectangle. Keep a position to write a word.


# Architechture
The Architecture is explained in provided [report](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/use_case_architecture%20final%20(2).pptx)

![Output sample](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/archi/Screenshot%20(5).png)

# Interface 1: ISL (images) to alphabets (text) Model architecture
+ In the first interface, initially, the position of the user’s hands captured in bounding box is taken in the form of image streamed in real time. A series of the real time frames is being fed to the model. 
+ The classification model has been trained on 26 alphabets and 3 additional gestures(3000 images for each) i.e. nothing, space and delete. The model follows the architecture of Inception ResNet v3. The output of the model is in the form of text that is being fed to the front end through our server.
+ Each frame gives an alphabet which is being appended to the sequence printed and converted to speech through GTTS at the end of the processing of all the real time frames.


![Output sample](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/archi/Screenshot%20(6).png)

![Output sample](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/archi/Screenshot%20(7).png)

# Interface 2: ISL (Videos) to alphabets/gestures (text) Model architecture
+ This API seeks upon taking a recorded video taken through the react interface and  providing it to the server at the backend.
+ The server seeks upon feeding the video in our deep learning model which is based upon the LSTM network as it learns through RNN to identify gesture by storing the hand movements retrieved from each frame of the provided video dataset(It has memory) trained on 2600 videos 100 belonging to each gesture.
+ The output of this model is provided to the server which communicated with the frontend in order to show the results.
+ The result such as ‘good-afternoon’ is then converted into audio using gTTs, a google text to speech API. 

The training of the model is done through following architecture:
Extract frames from gesture videos
Training of frames on Inception resnet V3 model
Each Video is represented by a sequence of n dimensional vectors (probability distribution or output of softmax) one for each frame. Here n is the number of classes.
Train the RNN model on the softmax based representation of gestures for 10 epochs and save the model.
Predict the labels of the softmax based representation of the test videos.Predictions and corresponding gold labels for each test video will be displayed.

![Output sample](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/archi/Screenshot%20(8).png)

# Interface 3: Audio to gestures(video) GUI Interface
+ This model is based upon taking  Speech as input through microphone using PyAudio, an open source interface based upon converting speech into text. The Speech recognition using Google Speech API. 
+ The input text is processed through a natural language processing model based on a sequences (preserves word order) representation and the output in form of an optimized text is received through appropriate classifier.
+ To each input text we have a corresponding video of a word/ image of an alphabet retrieved as we provide the corresponding text taken through simple list structure and operating system operations

# Test Results
![Output sample](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/results/giffff.gif)

![alt text](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/results/1.PNG)

![alt text](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/results/2.PNG)

![alt text](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/results/3.PNG)

![alt text](https://github.com/chahatgoyal/Indian-Sign-Language/blob/master/results/4.PNG)

# links for video test results
Working demo of our models can be seen in the following youtube videos:
[ISL (images) to alphabets (text)(live streaming)](https://www.youtube.com/watch?v=d5kGSsQPO-E&feature=youtu.be)
[ISL (Videos) to alphabets/gestures (text)(test images)](https://www.youtube.com/watch?v=E1d6CupAJHQ&feature=youtu.be)
[ISL (Videos) to alphabets/gestures (text)]https://www.youtube.com/watch?v=bW8oX36kigw&feature=youtu.be
[Audio to gestures(video)] https://www.youtube.com/watch?v=LJ_DwAnrxb0&feature=youtu.be







