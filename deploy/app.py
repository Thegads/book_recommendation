import os.path
from flask import Flask, render_template ,request, redirect, url_for
import os
import json
import run_backend
import get_data
import ml_utils
import time

app = Flask(__name__)

def get_predictions():
    livros = []
    
    novos_livros_json = 'novos_books.json'
    if not os.path.exists(novos_livros_json):
        run_backend.update_db()
        
    last_update = os.path.getmtime(novos_livros_json) * 1e9
    
    with open('novos_books.json', 'r') as data_file:
        for line in data_file:
            line_json = json.loads(line)
            livros.append(line_json)
            
    predictions = []
    for livro in livros:
        predictions.append(
                            {"link":livro['link'],
                             "livros":livro['book'],
                             "score": "{0:.0%}".format(round(livro['score'],2)),
                             "image":livro['image']
                           }
                            )

    predictions = sorted(predictions, key = lambda x: x['score'], reverse = True) [:20]
    
    return predictions, last_update

@app.route('/')
def main_page():
    
    predictions, last_update = get_predictions()
    
    return render_template("index.html", predictions = predictions) 

#This section is new, it will handle the user input    
def get_predictions_updated(data):
        livros2 = []

        novos_livros_json2 = 'novos_books2.json'
        if not os.path.exists(novos_livros_json2):
            run_backend.user_update(data)

        last_update2 = os.path.getmtime(novos_livros_json2) * 1e9

        with open('novos_books2.json', 'r') as data_file2:
            for line in data_file2:
                line_json2 = json.loads(line)
                livros2.append(line_json2)

        predictions2 = []
        for livro in livros2:
            predictions2.append(
                                {"link":livro['link'],
                                 "livros":livro['book'],
                                 "score": "{0:.0%}".format(round(livro['score'],2)),
                                 "image":livro['image']
                               }
                                )

        predictions2 = sorted(predictions2, key = lambda x: x['score'], reverse = True) [:20]

        return predictions2

@app.route('/handle_data', methods=['POST'])
def handle_data():
    if request.method == 'POST':
        nq = request.form['newquery']
        
    return redirect(url_for('new_index', inputvalue = nq))

@app.route('/<inputvalue>')
def new_index(inputvalue):
    query = ['{}'.format(inputvalue)]
    
    predictions2 = get_predictions_updated(query)
    
    return render_template("index_up.html", predictions = predictions2)
    
    
if __name__ == '__main__':
    app.run(debug = True, host = 'localhost')