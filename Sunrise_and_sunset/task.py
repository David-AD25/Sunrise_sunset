import requests 
import datetime

# API Parameters
parameters = {
    "lat" : 53.480759,
    "lng": -2.242631,
    "formatted" : 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params= parameters )

# Raise an exception for any error code : 
response.raise_for_status()

# Turn the data to a json 
data = response.json()


print(data["results"]["sunset"].split("T")[1].split(":")[0])

# Assinging the sunrise and sunset times to variables
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# Made them into a tupple 
sun_times = (sunrise, sunset)

# We are splitting the sunrise format into 2 halves of a list 
# print(sunrise.split("T")[1].split(":")[0])

current_time = datetime.datetime.now()

print(sunrise)
print(sunset)
print(current_time.hour)


# Try to pull the chanegs mate 
# Created and switched to new trial-branch , made some changes now pushing 