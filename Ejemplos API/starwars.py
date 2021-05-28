import requests

main_api="https://swapi.dev/api/"
resources = requests.get("https://swapi.dev/api/").json()
print("STARWARS API\n")
print(resources['people'])
print(resources['planets'])
print(resources['films'])

while True:
    search=input("define a resource withing the platform: ")
    if search == "quit" or search == "q":
        break

    elif search == "starships":
        print("choose a value ID from 0 to 36")
        search2=input("choose ID: ")
        url=main_api+search+"/?search="+search2
        json_data=requests.get(url).json()
        print("resource count: ",json_data["count"])
        print("resource name: ",json_data["results"][0]["name"])
        movies=json_data["results"][0]["films"][0:6]
        for i in movies[0:6]:
            print(i)

    elif search =="people":
        url=main_api+search+"/?search="
        json_data=requests.get(url).json()
        print("resource count: ",json_data["count"])
        for i in json_data["results"][0:36]:
            print("===========================================")
            print("name of character: ",i["name"],"|","height: ",i["height"])
            print("hair color: ",i["hair_color"],"|","eye color",i["eye_color"])
            print("============================================")



