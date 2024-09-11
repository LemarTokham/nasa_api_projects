# Atronomy Picture of the Day
import requests

# Todays image
endpoint = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
response = requests.get(endpoint).json()
# store image in a file
img_url = requests.get(response["url"])
with open("apod.jpg", mode="wb") as file:
    file.write(img_url.content)

# output image description
img_descption = response["explanation"]
print(img_descption)

# create a line break for easier reading
for i in range(100):
    print("-", end="")
print()


# output image of Sept 8 (as of current date that would count as yesterday)
query_params = {"date": "2024-09-10"}
response = requests.get(endpoint, params=query_params).json()

prev_img_url = requests.get(response["url"])
with open("prev_img.jpg", mode="wb") as file:
    file.write(prev_img_url.content)

prev_desciption = response["explanation"]
print(prev_desciption)


# create a line break for easier reading
for i in range(100):
    print("-", end="")
print()


# Custom date image
custom_date = input("Please enter your custom date in the format YYYY-MM-DD: ")

# create a line break for easier reading
for i in range(100):
    print("-", end="")
print()

query_params = {"date": custom_date}
response = requests.get(endpoint, params=query_params).json()

custom_url = requests.get(response["url"])
with open("custom_img.jpg", mode="wb") as file:
    file.write(custom_url.content)

custom_desctiption = response["explanation"]
print(custom_desctiption)