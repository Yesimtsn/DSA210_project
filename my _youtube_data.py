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
#Extract and format the data into different dictinaries and arrays to simplify the visulization process
from datetime import datetime
from itertools import islice

def category_count(filename):
    category_dict={}
    with open(filename+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        if 'categoryId' in item:
            category_id = item['categoryId']
            # Update the count of the category in the dictionary
            if category_id in category_dict:
                category_dict[category_id] += 1
            else:
                category_dict[category_id] = 1
    print(category_dict)
    print(len(category_dict))
    return category_dict

def duration_to_minutes(duration_str):
    try:
        total_seconds = int(duration_str)
        result=total_seconds / 60.0
        return round(result)
    except (ValueError, TypeError):
        print('error')
        return 0 

def category_duration(filename):
    category_duration_dict = {}
    with open(filename+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        category_id = item.get('categoryId')
        duration = duration_to_minutes(item.get('durationv'))
        
        if category_id and duration:
            if category_id in category_duration_dict:
                category_duration_dict[category_id] += duration
            else:
                category_duration_dict[category_id] = duration
    print(category_duration_dict)
    return category_duration_dict

def parse_date(watched_at):
    try:
        dt = datetime.fromisoformat(watched_at.replace('Z', '+00:00'))  # Handle ISO 8601 date with Z
        return dt.strftime('%Y-%m-%d')  # Format as "YYYY-MM-DD"
    except (ValueError, TypeError):
        return None  # Skip invalid dates
    
def date_duration(filename):
    daily_duration = {}
    with open(filename+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        watched_at = item.get('watched_at')
        duration = duration_to_minutes(item.get('durationv'))
        date = parse_date(watched_at)
        
        if date and duration:
            if date in daily_duration:
                daily_duration[date] += duration
            else:
                daily_duration[date] = duration
   
    for key, value in list(daily_duration.items())[-5:]:
        print(f"{key}: {value}")
    return daily_duration

def extract_category_data(filename):
    with open(filename+'.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    category_date = []
    for item in data:
        category_id = item.get('categoryId')
        watched_at = item.get('watched_at')
        date = parse_date(watched_at)
        if category_id and date:
            category_date.append((category_id, date))
    print(category_date[0])
    return category_date
