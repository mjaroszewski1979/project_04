from flask import Flask, render_template, url_for

app = Flask(__name__)
app.secret_key = 'secretkey1'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

if __name__=='__main__':
    app.run(debug=True)

