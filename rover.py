import requests
# NASA API
# parameters to specify the sol (day) and camera used to take the photos
query_params = {
    "sol": "1000", 
    "camera": "fhaz",
    "api_key": "DEMO_KEY"
}
# link to access all the photos fromt the curiosity rover
endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
response = requests.get(endpoint, params=query_params).json()

# pictures taken on sol 1000
# img 1
img_url = response["photos"][0]["img_src"]
img_response = requests.get(img_url) # HTTP get method is called on provided link
print(img_response.headers.get("Content-Type")) 
with open("rover.jpg", mode="wb") as file:
    file.write(img_response.content)

# img 2
img_url_two = response["photos"][1]["img_src"]
img_response_two = requests.get(img_url_two)
with open("rover_two.jpg", mode="wb") as file:
    file.write(img_response_two.content)

