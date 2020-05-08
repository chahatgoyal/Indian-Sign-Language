

import cv2, numpy as np
import utils



def recognise_hand_pose(image, directly_from_hand=False, model_path='Models/digits_and_letters.sav', using_stabilization=False, no_of_frames=1):


    import pickle
    from sklearn.neighbors import KNeighborsClassifier

    if not directly_from_hand:
        mask = utils.segment(image)
        face, foundFace = utils.detect_face(image)
        mask = utils.eliminate_face(face, foundFace, mask)

        if using_stabilization: mask = utils.stabilize(foundFace, no_of_frames, image, face, mask)

        hand = utils.get_my_hand(mask)
        if hand is False: return 'No hand pose in image'
        features = utils.extract_features(hand)
    else: features = utils.extract_features(image)

    classifier = pickle.load(open(model_path, 'rb'))
    hand_pose = classifier.predict([features])[0]

    return hand_pose


class Gesture:
    '''
   

    Initialise an instance of this class, and use the add_frame function to pass each Gesture frame into the instance. At last, use classify_gesture to get Classification result.

    Object stabilization is still in its early stages and may not be reliable. If you want to use, set the using_stabilization parameter in constructor to True.
    '''
    
    def __init__(self, using_stabilization=False):
        
        from sklearn.externals import joblib
        from utils import HandMotionRecognizer
        import os

        self.__observations = []
        self.__using_stabilization = False
        self.__no_of_frames = 0
        self.__motion = HandMotionRecognizer()
        
    def add_frame(self, image):
       
        mask = utils.segment(image)
        face, foundFace = utils.detect_face(image)
        mask = utils.eliminate_face(face, foundFace, mask)

        if self.__using_stabilization: mask = utils.stabilize(foundFace, self.__no_of_frames + 1, image, face, mask)
        hand, hand_contour = utils.get_my_hand(mask, True)
        
        hand_pose, direction = 'None', 'None'

        if hand_contour is not None: motion_detected = self.__motion.get_hand_motion(hand_contour)
        else: return

        if not motion_detected: hand_pose = recognise_hand_pose(hand, directly_from_hand=True, model_path='Models/gesture_signs.sav')
        else: direction = motion_detected
                
        self.__observations.append((hand_pose,direction))
        self.__no_of_frames += 1

    def classify_gesture(self, return_score=False):
       
        import hmmlearn, numpy as np, os
        from sklearn.externals import joblib

        kfMapper = {'Up':0,'Right':1,'Left':2,'Down':3,'ThumbsUp':4, 'Sun_Up':5, 'Cup_Open':6, 'Cup_Closed':7, 'Apple_Finger':8, 'OpenPalmHori':9, 'Leader_L':10, 'Fist':11, 'That_Is_Good_Circle':12}
        dir = "./Models/GestureHMMs"
        Models = []
        ModelNames = []
        
        for model in os.listdir(dir):
            Models += [joblib.load(dir+"/"+model)]
            ModelNames += [model.split(".")[0]]

        testInputSeq = []
        for elem in self.__observations:
            if elem[0] == 'None':
                testInputSeq += [kfMapper[elem[1]]]
            else:
                testInputSeq += [kfMapper[elem[0]]]
        
        maxScore = float('-inf')
        testInputSeq = np.reshape(np.array(testInputSeq),(-1,1))
        recognizedGesture = "--"
        for i in range(len(Models)):
            scoreTemp = Models[i].score(testInputSeq)
            if scoreTemp > maxScore:
                maxScore = scoreTemp
                recognizedGesture = ModelNames[i]
        if return_score: return (recognizedGesture,maxScore)
        else: return recognizedGesture
    
    def get_observations(self): return self.__observations
