from EmotionDetection.emotion_detection import emotion_detector
import unittest

def test_emotion_detector():
    testJoy = emotion_detection('I am glad this happened')
    testAnger = emotion_detection('I am really mad about this')
    testDisgust = emotion_detection('I feel disgusted just hearing about this')
    testSadness = emotion_detection('I am so sad about this')
    testFear = emotion_detection('I am really afraid that this will happen')
    ok = 'joy' in testJoy and 'anger' in testAnger and 'disgust' in testDisgust and 'sadness' in testSadness and 'fear' in testFear 
    print(f"Is ok {ok}")
    