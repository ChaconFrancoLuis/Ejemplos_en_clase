import requests

print("AGE OF EMPIRES API!!")
url ="https://age-of-empires-2-api.herokuapp.com/api/v1/civilizations"

send=requests.get(url).json()

for a in send["civilizations"][0:32]:
    print(type(a))
    print("civilization name: |",a["name"])
    print("expansion name: |",a["expansion"],"\n")