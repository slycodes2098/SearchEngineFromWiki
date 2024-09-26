import requests
from bs4 import BeautifulSoup
from constant import search_engine_url
import sqlite3

table_name = "History"
db_name = "User History"
connection = r"Search Engine/UserHistory.db"

class DataBaseManager:
    def __init__(self):

        self.table_name = table_name
        self.db_name = db_name
        self.connection = sqlite3.connect(connection)
        self.cursor = self.connection.cursor()
        self.create_table()


    def create_table(self):
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            SEARCH_WORD TEXT NOT NULL,
                            SEARCH_RESULT TEXT NOT NULL
                            )""")
        self.connection.commit()


    def insert_data(self, search_word, search_result):
        sql_query = f"INSERT INTO {table_name} (SEARCH_WORD, SEARCH_RESULT) VALUES (?,?)"
        self.cursor.execute(sql_query, (search_word, search_result))
        self.connection.commit()




class SearchEngine:
    result = []

    def search(self , word):
        search_word = self.construct_Word(word)
        result_text = ""
        if search_engine_url:
            url = search_engine_url + search_word
            result = requests.get(url)
            if result.status_code == 200:   
                data = BeautifulSoup(result.content, 'html.parser')
                paragraphs = data.find_all('p')
                for paragraph in paragraphs:
                    result_text += paragraph.get_text()
                return(result_text)
            elif result.status_code == 404:
                return Exception("Seach Parameter not found")
            
            elif result.status_code ==500:
                return Exception("A server error occured")
            else:
                print("Failed to retrieve page")
        else:
            return None

    def construct_Word(self, word:str)-> str:
        try:
            if word:
                word.strip()
                return word.title().replace(" ","_")
            else:
                raise Exception
        except:
            return None
        

