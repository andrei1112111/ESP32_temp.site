import os
from flask import request, render_template
from flask import Flask
import json

app = Flask(__name__)

led, temp, comand = 0, 'None', ''


@app.route("/control", methods=['POST', 'GET'])
def index():
    global led, temp, comand
    if request.method == 'POST':
        if 'foo' in request.form.keys():
            comand = 'temp'
        else:
            comand = 'led'
        print(comand)
    text = 'Зажечь светодиод' if led else 'Погасить светодиод'
    return render_template(
        'control.html',
        data={
            'text': text,
            'temp': temp
        }
    )


@app.route("/command")
def command():
    global led, comand
    h = comand
    if comand == 'led':
        led = 0 if led else 1
    comand = ''
    return h


@app.route("/send", methods=['POST'])
def send():
    global temp, led
    if request.method == 'POST':
        temp = f"{json.loads(request.get_data())['temperature']}°С"
        print(temp)
    return '1'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
