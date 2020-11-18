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


def user_update(new_queries):
    with open('novos_books.json', 'w+') as output2:
        for query2 in new_queries:
            for page2 in range(1,2):
                search_page2 = donwload_search_page(query2, page2)
                book_list2 = parse_search_page(search_page2)
                
                for book2 in book_list2:
                    book_page2 = download_book_page(book2)
                    book_json_data2 = parse_book_page(book_page2)
                        
                    p2 = compute_prediction(book_json_data2)                   
                    
                    book_name2 = book_json_data2['title']
                    link2 = 'https://www.amazon.com'+book2
                    image2 = book_json_data2['image']
                    score2 = p2
                    
                    data_front2 = {"book": book_name2, "score": score2, "link": link2, "image": image2}
                    data_front2['update_time'] = time.time_ns()
                    
                    print(data_front2)
                    output2.write('{}\n'.format(json.dumps(data_front2)))
    return True