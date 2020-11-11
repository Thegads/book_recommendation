from get_data import *
from ml_utils import *
import time

queries = ['natural+language+processing']

def update_db():
    with open('novos_books.json', 'w+') as output:
        for query in queries:
            for page in range(1,2):
                search_page = donwload_search_page(query, page)
                book_list = parse_search_page(search_page)
                
                for book in book_list:
                    book_page = download_book_page(book)
                    book_json_data = parse_book_page(book_page)
                        
                    p = compute_prediction(book_json_data)                   
                    
                    book_name = book_json_data['title']
                    link = 'https://www.amazon.com'+book
                    image = book_json_data['image']
                    score = p
                    
                    data_front = {"book": book_name, "score": score, "link": link, "image": image}
                    data_front['update_time'] = time.time_ns()
                    
                    print(data_front)
                    output.write('{}\n'.format(json.dumps(data_front)))
    return True