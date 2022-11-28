from flask import Flask
from flask import render_template
import jyserver.Flask as jsf
from spelling import *

app = Flask(__name__)
@jsf.use(app)
class App:
    def __init__(self):
        inputtext = self.js.document.getElementById("inputtext").innerText = list_kata
        print (inputtext)
    
@app.route('/')
def index():
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
