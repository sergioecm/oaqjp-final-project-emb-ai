from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Sergioecm")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    # get texto de la solicitud
    text_to_analyze = request.args.get('textToAnalyze')
    
    # call detector de emociones
    response = emotion_detector(text_to_analyze)

    # Extract data
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Format response
    result_text = (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} y 'sadness': {sadness}. La emoción dominante es {dominant_emotion}."
    )

    return result_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

