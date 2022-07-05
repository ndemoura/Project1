import requests

url = "https://genius-song-lyrics1.p.rapidapi.com/search"
print("Enter a song and get the artist's name: ")
userInput = input()

def find_song(userInput):

	artist = "Unknown"
	querystring = {"q": userInput,"per_page":"10","page":"1"}

	headers = {
		"X-RapidAPI-Key": "43fb6ee4a1msh7568a7151ba2e23p175eb7jsnf3f4dd62ad49",
		"X-RapidAPI-Host": "genius-song-lyrics1.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	json = response.json()
	if len(json["response"]['hits']) < 3:
		return artist
	return json["response"]['hits'][0]["result"]["artist_names"]

print(find_song(userInput))