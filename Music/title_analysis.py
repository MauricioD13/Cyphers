from hermetrics.levenshtein import Levenshtein
import requests
import json
import base64
url = "https://shazam.p.rapidapi.com/songs/detect"

binaryfile = open("Downloads/Electronica_actual/Vini Vici  -  Namaste.mp3",'rb')
binarydata = binaryfile.read()
binaryfile.close()


b64_data =




payload = "Generate one on your own for testing and send the body with the content-type as text/plain"
headers = {
    'content-type': "text/plain",
    'x-rapidapi-host': "shazam.p.rapidapi.com",
    'x-rapidapi-key': "07b7fd1a81mshd5cf37410df96d6p12a1b3jsn6bbb5b752911"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
parsed = json.loads(result.text)
print(json.dumps(parsed, indent=4, sort_keys=True))

#lev = Levenshtein()



"""
for idx, value in enumerate(new_names):
    dist = lev.distance(good_names[idx],new_names[idx])
    norm = lev.normalized_distance(good_names[idx],new_names[idx])
    sim = lev.similarity(good_names[idx],new_names[idx])
    print(f"Nuevo: {new_names[idx]}, Bueno: {good_names[idx]}")
    print(f"Distancia:{dist}, Normalizada: {norm}, Similitud: {sim}")
    print('--------------------------------------------')
"""
#https://github.com/kampamocha/hermetrics
#https://medium.com/@diego.campos.sobrino/m%C3%A9tricas-de-similitud-para-cadenas-de-texto-parte-iv-biblioteca-hermetrics-para-python-33404f0ddb70
#https://pypi.org/project/hermetrics/