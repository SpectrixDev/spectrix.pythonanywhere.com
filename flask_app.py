from flask import Flask, request, redirect
import re

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("http://spectrix.technology/")

@app.route('/botsaber')
def botsaber():
    try:
        key = request.args.get('key')
        if any(char.isdigit() or char.isalpha() for char in key) and len(key) == 4:
            return redirect(f"beatsaver://{(re.sub('[^0-9a-zA-Z]+', '', key))}", code=302)
        else:
            return "That doesn't seem to be a valid key..."
    except:
        return "No args found. Something wrong? Check here: https://github.com/SpectrixOfficial/spectrix.pythonanywhere.com/"
