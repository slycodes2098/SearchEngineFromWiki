from searchengine import SearchEngine
from searchengine import DataBaseManager
flag = False
google = SearchEngine()
database = DataBaseManager()




def save_user_result(search_input, search_result):
    while True:
        try:
            save_result = input("Enter Y to save your result\n"
                                "Enter any other key to continue\n")
            if save_result.lower() == "y" or save_result.lower() == "yes":
                database.insert_data(search_input, search_result)

            while True:
                try:
                    search_again = input("Enter Y to search again\n")
                    if search_again.lower() == "y" or search_again.lower() == "yes":
                        test_engine() 
                    else:
                        print("Thank you for using this search egine")
                        exit()
                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)




def print_paragraphs(user_input, result):
    while True:
        try:
            lines = input("How many paragraphs of the result do you want to see?\n")
            if lines.isdigit():
                lines = int(lines)
                paragraphs = result.replace("\n","\n-- \n").split("\n--")  
                result = "".join(paragraphs[:lines])
                print(f"Search Results for '{user_input}':\n{result.replace("\n","\n"*3)}\n\n")
                break
            else:
                print("Enter digits only")
                continue
        except Exception as e:
            print(e)



        
    


def test_engine():
    try:
        print("::::::::Welcome to Search Engine::::::::::")
        while True:
            user_input = input("WHAT WORD DO YOU WANT TO SEARCH TODAY?\n")
            if user_input:
                result = google.search(user_input).strip()
                while True:
                    try:
                        display = input("Enter Y to display all your search results\n"
                                        "Enter N to continue\n")
                        if display.lower() == "y" or display.lower() == "yes":
                            print(f"Search Results for '{user_input}':\n{result.replace("\n","\n"*3)}\n\n")
                            save_user_result(user_input, result)
                            break
                        else:
                            print_paragraphs(user_input, result)
                            save_user_result(user_input, result)
                            break
                    except Exception as e:
                        print(e)
    except Exception as e:
        print(e)





test_engine()