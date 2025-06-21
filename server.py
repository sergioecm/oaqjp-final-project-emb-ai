"""
Módulo principal del servidor Flask para la detección de emociones.
Este módulo maneja las rutas HTTP y la integración con el analizador de emociones.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection Sergioecm")

@app.route("/")
def render_index_page():
    """
    Renderiza la página principal de la aplicación.

    Returns:
        str: Contenido HTML de index.html renderizado.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Maneja la solicitud GET para analizar el texto proporcionado por el usuario.
    Llama al detector de emociones y devuelve un mensaje formateado.

    Returns:
        str: Resultado del análisis de emociones o mensaje de error.
    """
    # get texto de la solicitud
    text_to_analyze = request.args.get('textToAnalyze')

    # call detector de emociones
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

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
