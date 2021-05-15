# Fill in this file with the code from parsing JSON exercise
import json
import yaml

with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)

print(type(ourjson))

print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))
print("-------------------------------------------------------")

print("\n\n---")
a = yaml.dump(ourjson)
print(type(a))