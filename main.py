from flask import Flask, request, render_template, url_for, redirect
from symspellpy import SymSpell, Verbosity
import pkg_resources

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deteksi')
def deteksi():
    return render_template('deteksi.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    hasil = request.form['textoutput']
    input = request.form['textinput']

    
    #lookup suggestions for multi-word input strings (supports compound splitting & merging)
    sentence = input.split()
    #initialize
    sym_spell = SymSpell()
    # create dictionary
    path_corpus = "kompas.txt"
    sym_spell.create_dictionary(path_corpus)

    for kata in sentence:
                suggestion = suggestions = sym_spell.lookup_compound(
    input, max_edit_distance=2, transfer_casing=True,
)

            #display term and edit distance
                for suggestion in suggestion:
                    hasil = suggestion
    return render_template('deteksi.html', hasil = hasil, input=input )
if __name__ == '__main__':
    app.run()