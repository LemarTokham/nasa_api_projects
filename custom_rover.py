# Images of Mars fetched by entering a custom date
import requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "DEMO_KEY"
custom_date = input("Earth Date (YYYY-MM-DD): ")
query_params = {"api_key": api_key, "earth_date": custom_date}
response = requests.get(endpoint, params=query_params).json()
try:
    
    img_url = requests.get(response["photos"][0]["img_src"])
    with open("custom_rover.jpg", mode="wb") as file:
        file.write(img_url.content)
except IndexError:
    print("No image data")

