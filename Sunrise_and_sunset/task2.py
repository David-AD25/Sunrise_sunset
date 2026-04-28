import requests 
import datetime as dt


def iss_pos():
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

    return(iss_position)





# Sunset and Sunrise API : 

# API Parameters
parameters = {
        "lat" : 51.507351,
        "lng": -0.127758,
        "formatted" : 0,
    }

response = requests.get(url="https://api.sunrise-sunset.org/json", params= parameters )

    # Raise an exception for any error code : 
response.raise_for_status()

    # Turn the data to a json 
data = response.json()

    # Assinging the sunrise and sunset times to variables
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
   



my_lat = 51.507351
my_lng = -0.127758
my_pos = (my_lat, my_lng)
# print(iss_pos())
# print(my_pos)



current_time = dt.datetime.now().hour
print(current_time)



if (current_time >= sunset and current_time < sunrise) :
    print("email will be sent")

else : 
    print("not dark yet")

