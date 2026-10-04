import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    if response.status_code == 200:
        fr = response.json()
        text_response = fr['emotionPredictions'][0]['emotion']
        print(text_response)
    else:
        text_response = {'text':{'none':0.00}}
    return {'text':text_response}
