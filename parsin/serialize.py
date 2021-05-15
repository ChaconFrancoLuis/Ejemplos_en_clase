

import dicttoxml
import requests

auth = {
  "user": {
    "username": "myemail@mydomain.com",
    "key": "90823ff08409408aebcf4320384"
  }
}

get_services_query = "https://myservice.com/status/services"

xmlstring = dicttoxml.dicttoxml(auth)

#myresponse = requests.get(get_services_query,auth=xmlstring)  
print(xmlstring)