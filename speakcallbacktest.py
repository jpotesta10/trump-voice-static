import os
import time
from flask import Flask, request, Response, render_template
from elevenlabs import generate, set_api_key

app = Flask(__name__)

# Set the Eleven Labs API key
api_key = '9fd8b38cd4c1855c78d02160bc8310ac'
set_api_key(api_key)

@app.route('/')
def home():
    time.sleep(5)  # Delay for 5 seconds
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_audio():
    time.sleep(25)  # Delay for 25 seconds
    data = request.json
    text = data.get('text')
    audio = generate(text=text, voice='Joe American')
    return Response(audio, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
