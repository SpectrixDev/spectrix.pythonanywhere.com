from flask import Flask, request, redirect
import re

app = Flask(__name__)

@app.route('/')
def bruh():
    try:
        key = request.args.get('key')
        if any(char.isdigit() or char.isalpha() for char in key) and len(key) == 4:
            return redirect(f"beatsaver://{(re.sub('[^0-9a-zA-Z]+', '', key))}", code=302)
        else:
            return "That doesn't seem to be a valid key..."
    except:
        return """Welcome to my website.\n
        You can put the following args at the end of the url: key (botsaber).\n
        My actual website: https://spectrixofficial.github.io/.\n
        Source code and website explanation here: https://github.com/SpectrixOfficial/spectrix.pythonanywhere.com"""
