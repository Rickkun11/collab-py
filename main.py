from flask import Flask
from flask import render_template
import jyserver.Flask as jsf
from spelling import *

app = Flask(__name__)
@jsf.use()
class App:
    def __init__(self):
        self.console.log(list_kata)

    
@app.route('/')
def index():
        return App.render(render_template('index.html'))

if __name__ == '__main__':
    app.run()