from dotenv import load_dotenv
import os
import requests 
import json



load_dotenv()
api_key = os.getenv("API_KEY")



base_url = "https://api.rawg.io/api"
endpoint = "/games"
params = {
    "key": api_key,
    "search": "Splatoon" 
}

response = requests.get(base_url + endpoint, params=params)
'''if response.status_code == 200:
    game_data = response.json()
    print(game_data)
else:
    print(f"Error: {response.status_code}")'''

if response.status_code == 200:
    game_data = response.json()
    results = game_data.get("results", [])  #Get the list of games from 'results'
    
    if results:  #Check if any games were returned
        for game in results[:1]:  #Gets the top search result
            platforms = [platform_info["platform"]["name"] for platform_info in game.get("platforms", []) if platform_info.get("platform")]
            filtered_data = {
                "name": game.get("name"),
                "released": game.get("released"),
                "rating": game.get("rating"),
                #"playtime": game.get("playtime"),
                "background_image": game.get("background_image"),
                "esrb_rating": game.get("esrb_rating", {}).get("name"), 
                #"esrb_rating": game.get("esrb_rating")
                "platforms": platforms
            }
            print(filtered_data) #Print basic game info
    else:
        print("No games found in the response.")
else:
    print(f"Error: {response.status_code}")