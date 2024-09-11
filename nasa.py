import requests
# NASA API
query_params = {
    "sol": "1000", 
    "camera": "fhaz",
    "api_key": "DEMO_KEY"
}
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"


response = requests.get(endpoint, params=query_params).json()
img_url = response["photos"][0]["img_src"]
response = requests.get(img_url)
print(response.headers.get("Content-Type"))
with open("rover.jpg", mode="wb") as file:
    file.write(response.content)