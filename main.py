from flask import Flask
from flask import render_template
import jyserver.Flask as jsf
from symspellpy import SymSpell, Verbosity


app = Flask(__name__)
class App:
    def __init__(self):
        # initialize
        sym_spell = SymSpell()

        # create dictionary
        path_corpus = "kompas.txt"
        sym_spell.create_dictionary(path_corpus)

        #lookup suggestions for multi-word input strings (supports compound splitting & merging)
        list_kata = ''
        sentence = list_kata.split()

        for kata in sentence:
            maxEditDistanceLookup = 2
            include_unknown = True
            suggestion = sym_spell.lookup(kata, Verbosity.TOP, maxEditDistanceLookup, include_unknown)

        #display term and edit distance
            for s in suggestion:
                print(s.term, end=' ')
        
        textoutput = self.js.document.getElementById("outputtext")
        textinput = self.js.document.getElementById("textinput").innerHTML = list_kata


    
@app.route('/')
def index():
        return App.render(render_template('index.html'))

if __name__ == '__main__':
     app.run()













