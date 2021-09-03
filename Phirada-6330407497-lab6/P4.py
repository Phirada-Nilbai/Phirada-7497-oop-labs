import json
filename = "hobbies.json"
with open(filename, 'w') as file_obj:
    data = { "firstName": "Jane", "lastName": "Doe",
          "hobbies": ["running", "sky diving", "singing"]}
    json.dump(data,file_obj)

with open(filename, 'r') as file_obj:
    data = json.load(file_obj)
    text = ['has', 'hobbies', 'as', 'fun', 'programming', 'language'] #hard code TT
    print(data["firstName"],'has hobbies as running, sky diving, singing')
