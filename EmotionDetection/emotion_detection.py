import requests
import json

def emotion_detector(text_to_analyze):
    """
    Sends text to Watson NLP Emotion Predict API and returns a formatted dictionary
    containing individual emotion scores and the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send request
    response = requests.post(url, json=myobj, headers=header)
    
    # Convert response text to dictionary using json.loads
    formatted_response = json.loads(response.text)
    
    # Extract emotions dictionary from response structure
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Find the dominant emotion (emotion with the highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Return formatted output dictionary
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
