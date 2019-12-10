from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return render_template('cindex.html')

@app.route('/hello/<name>')
def hello(name):
    if name == Nikij
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        time.sleep(1)


    return render_template('page.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

