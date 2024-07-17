"""
Oscar Alvarado
Cst 205
7/10/2024
"""
#task 1 i installed flask and got no errors 
#task 2
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello_world():
    return "<p>Smirth's favorite acronym is ASAP because of A$AP Rocky</p>"   
@app.route('/Oscar')
def hello_Oscar():
    return render_template('templates.html')