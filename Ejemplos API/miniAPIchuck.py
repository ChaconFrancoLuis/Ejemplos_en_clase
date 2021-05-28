#libreria requests que encapsula los metodos HTTP (get,post, put,patch,delete)
import requests

#variable url que utiliza URI base para peticion inicial.
url = "https://api.chucknorris.io/jokes/categories"

#variable json_data que utiliza o ejecuta el metodo get
json_data = requests.get(url).json()

print(json_data)

while True:
    search=input("choose the Joke Category: ")
    if search == "quit" or search == "q":
        break
    url2="https://api.chucknorris.io/jokes/random?category={}".format(search)
    json_data = requests.get(url2).json()
    print("================================================")
    print("here goes the joke....\n",json_data["value"])
