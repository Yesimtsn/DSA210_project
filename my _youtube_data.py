#Requested watch-history and search-history from Google Takeout
#Parse each video id of the watch and search history into a new array
#For watch-history video ids:
import json
with open('watch-history.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

watch_hist_ids = []  # List to store video IDs and watched times
watched_time_map = {}  # Dictionary to map video ID to its watched time

for item in data:
    if 'titleUrl' in item:
        url = item['titleUrl']
        
        if 'v=' in url:
            watch_hist_id = url.split('v=')[1].split('&')[0]  # Extract video ID
            watched_time = item.get('time')  # Extract watched timestamp
            
            if watch_hist_id and watched_time:
                watch_hist_ids.append(watch_hist_id)  # Store video ID
                watched_time_map[watch_hist_id] = watched_time  # Map video ID to watched time

print(f"Extracted {len(watch_hist_ids)} video IDs.")
#For the search-history video ids:
with open('search-history.json', 'r',encoding='utf-8') as file:
    data = json.load(file)

# Extract video IDs from search history
search_hist_ids = []
searched_time_map = {}  

for item in data:
    if 'titleUrl' in item:
        url = item['titleUrl']
        
        if 'search_query' in url:
            search_hist_id = url.split('search_query')[1].split('&')[0]  # Extract video ID
            searched_time = item.get('time')
            if search_hist_id and searched_time:
                search_hist_ids.append(search_hist_id) 
                searched_time_map[search_hist_id] = searched_time 

print(f"Extracted {len(search_hist_ids)} video IDs.")

#Fetch the relevant meta data of the watched and searched video ids
API_KEY = 'X'
youtube = build('youtube', 'v3', developerKey=API_KEY)
...
