import os.path
from flask import Flask, render_template ,request
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

if __name__ == '__main__':
    app.run(debug = True, host = 'localhost')