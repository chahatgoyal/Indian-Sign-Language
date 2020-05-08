import os
from subprocess import Popen

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

def switch(choice):
    if(choice == '1'):
        os.system('python3 classify_webcam.py')
    if(choice == '2'):
        os.system('python3 classify.py')
    if(choice == '3'):
        os.system('python3 gesture.py')
    if(choice == '4'):
        os.system('python3 main.py')



print("Hey! This is team altruists, you will see the major implementation of our code through this specific file. ")
print("--------------------------------------------------------------------------------------------------------------")

print("Select among the following 3 interfaces:")
print("press 1 for sign language to alphabet conversion in real time frame")
print("press 2 for sign language to alphabet conversion using test images")
print("press 3 for sign language to gesture conversion on our recorded video test data set")
print("press 4 for audio to sign langauge alphabet and gesture conversion")

#os.system('python3 classify_webcam.py')


choice = input("enter your choice : ")
#print(choice)
switch(choice)





