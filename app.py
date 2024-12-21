from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Path to the audio folder
AUDIO_FOLDER = os.path.join('static', 'audio')

@app.route('/')
def home():
    # List audio files in the static/audio folder
    audio_files = os.listdir(AUDIO_FOLDER)
    return render_template('index.html', audio_files=audio_files)

@app.route('/play/<filename>')
def play(filename):
    # Serve the selected audio file
    return send_from_directory(AUDIO_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
