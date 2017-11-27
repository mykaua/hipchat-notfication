#get all rooms

import requests
import json
import sys
from texttable import Texttable

tables = Texttable()
#https://gist.github.com/bdclark/4bc8ed06643e077fa620

token = ''#token

url = "https://hipchat_url/v2/room?start-index=0&max-results=1000&include-private='true'"
headers = {'Content-type': 'application/json'}
headers['Authorization'] = "Bearer " + token

r = requests.get(url, headers=headers)

t = r.status_code
#print json.dumps(r.json(), sort_keys=True, indent=2)
data = r.json()
for x in data['items']:
    id_room = x ['id']
    name_room = x['name']
    privacy = x['privacy']

    tables.add_rows([[ 'id_room', 'name_room', 'privacy_room'], [id_room, name_room, privacy]])

print tables.draw()

print t
