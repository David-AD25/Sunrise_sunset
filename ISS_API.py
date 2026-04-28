import requests

respone = requests.get(url="http://api.open-notify.org/iss-now.json")
# Function which raises an exception depending on this status code eg= 200 : success, 404: not found 
respone.raise_for_status()

# Function that turns the output of our requests into a json file (dictionary) 
data = respone.json()
print(data)


latitude = data["iss_position"] ["latitude"]
longitude = data["iss_position"] ["longitude"]

# Tuple of Lat and long : 
iss_position= (latitude,longitude)

print(iss_position)