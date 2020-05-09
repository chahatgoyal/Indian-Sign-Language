# Indian-Sign-Language
The Projects focuses on providing solution for communication barrier faced by people who are specially abled and use sign languages.


# Introduction

People with visual and hearing impairments find it difficult to communicate with those who do not know sign language. In case they want to communicate, they have to carry additional devices or need an interpreter which makes communication cumbersome. In many situations, the process becomes very inefficient and the user becomes very dependent.
 A computer vision based interactive mobile application which recognizes sign language through hand gestures, movement, orientation of fingers using image processing and converts it into text and speech. 
The application will use a deep learning model for the classification of images into words, sentences and alphabets. This predicted text will then be displayed on the screen of the user's  smartphone. 




# Installation Guide
Here are the steps and procedures you need to follow in order to execute our project

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

