from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Experience')
def experience():
    return render_template('experience.html')

@app.route('/Projects')
def projects():
    return render_template('projects.html')

@app.route('/Tune Trends')
def project_tune_trends():
    return render_template('projects/VA_project.html')

@app.route('/ML Project')
def project_ml():
    return render_template('projects/ML_project.html')

@app.route('/Riff Room')
def project_riff_room():
    return render_template('projects/SE_project.html')

@app.route('/Game Maker Projects')
def game_projects():
    return render_template('projects/game_projects.html')

@app.route('/Game Maker Projects/Botanical Brawl')
def game_botanical_brawl():
    return render_template('projects/Games/game_botanical_brawl.html')

@app.route('/Game Maker Projects/Platformer')
def game_platformer():
    return render_template('projects/Games/game_platformer.html')

@app.route('/Game Maker Projects/Scrolling Shooter')
def game_scrolling_shooter():
    return render_template('projects/Games/game_scrolling_shooter.html')

@app.route('/Game Maker Projects/Finite State Machines')
def game_fin_state_machines():
    return render_template('projects/Games/game_fin_state_machines.html')

@app.route('/Chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_message,
        max_tokens=150
    )
    reply = response.choices[0].text.strip()
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
