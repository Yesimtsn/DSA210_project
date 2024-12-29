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


#Fetch the relevant meta data of the watched and searched video ids
API_KEY = 'X'
youtube = build('youtube', 'v3', developerKey=API_KEY)

def parse_duration(duration_str):
    pattern = r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?"
    match = re.match(pattern, duration_str)
    
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds


def fetch_video_details(ids,map):
    all_hist_data = []  # List to store metadata
    batch_size = 50  # Maximum batch size allowed by API
    total_batches = (len(ids) + batch_size - 1) // batch_size  # Total number of batches

    for i in range(0, len(ids), batch_size):
        batch = ids[i:i + batch_size]
        try:
            # Fetch details for the current batch
            request = youtube.videos().list(part='snippet,contentDetails', id=','.join(batch))
            response = request.execute()

            # Extract relevant metadata
            for item in response['items']:
                video_id = item['id']
                duration =parse_duration(item['contentDetails']['duration'])
                video_data = {
                    'categoryId': item['snippet']['categoryId'],
                    'watched_at': map.get(video_id, 'Unknown'),  # Add watched time from map
                    'durationv':duration
                }
                all_hist_data.append(video_data)

            print(f"Batch {i // batch_size + 1}/{total_batches} fetched successfully.")
            time.sleep(1)  # Pause to avoid hitting rate limits

        except Exception as e:
            print(f"Error fetching batch {i // batch_size + 1}: {e}")
            time.sleep(5)  # Pause before retrying

    return all_hist_data
video_metadata = fetch_video_details(watch_hist_ids,watched_time_map)
# Save the data to a file for future analysis
import json
with open('video_metadata.json', 'w', encoding='utf-8') as f:
    json.dump(video_metadata, f, ensure_ascii=False, indent=4)
print(f"Fetched data for {len(video_metadata)} videos.")
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
#Dict of youtube categories:
youtube_categories = {
    1: "Film & Animation",
    2: "Autos & Vehicles",
    10: "Music",
    15: "Pets & Animals",
    17: "Sports",
    20: "Gaming",
    22: "People & Blogs",
    23: "Comedy",
    24: "Entertainment",
    25: "News & Politics",
    26: "Howto & Style",
    27: "Education",
    28: "Science & Technology",
    29: "Nonprofits & Activism",
    33: "Classics",
    44: "Trailers"
}
#Some functions for efficiency:
def eliminate_categories(category_counts,minute):
    return {category: minutes for category, minutes in category_counts.items() if minutes >= minute}
def dict_category_numbers_to_names(category_data, category_mapping):
    """Convert category numbers into names."""
    return {
            category_mapping[int(key)]: value 
            for key, value in category_data.items() 
            if int(key) in category_mapping
        }
def list_category_numbers_to_names(category_data, category_mapping):
    return {
            (category_mapping[int(key)], value)
            for key, value in category_data
            if int(key) in category_mapping
        }

#Create a dictionary of {categories: count}
cate_cou = category_count('video_metadata')
#Format the dictionary
category_counts =eliminate_categories (dict_category_numbers_to_names(cate_cou, youtube_categories),100)
import matplotlib.pyplot as plt

#Pie Chart Function:
def plot_category_pie_chart(category_counts):
    labels = category_counts.keys()
    print (category_counts)
    sizes = category_counts.values()
    colors = plt.cm.Paired(range(len(labels)))  # Use a colormap for consistent colors

    plt.figure(figsize=(10, 11))
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',  # Show percentages with 1 decimal place
        startangle=90,      # Start from the top of the circle
        colors=colors
    )
    plt.title("Categories Watched")
    plt.axis('equal')  # Equal aspect ratio to ensure the pie is a circle
    plt.show()
#Show the plot
plot_category_pie_chart(category_counts)


#Create category:duration dictionary and plot it
cate_dura =category_duration('video_metadata')
category_durations =eliminate_categories(dict_category_numbers_to_names(cate_dura, youtube_categories),1000)
def bar_chart(category_durations):
    categories = list(category_durations.keys())
    durations = list(category_durations.values())
    
    plt.bar(categories, durations, color='skyblue')
    
    plt.xlabel('Categories')
    plt.ylabel('Watch Duration(minutes)')
    plt.title('All Time Watch Durations of Categories')
    plt.xticks(rotation=45)
    #ama kaymışlar
    plt.show()
bar_chart(category_durations)

#Get date:duration info from the json file using the date_duration function
date_dura = date_duration('video_metadata')


#the plot function comes here

#Get categories to dates info
cate_date =extract_category_data('video_metadata')
category_date=list_category_numbers_to_names(cate_date, youtube_categories)

#scatter plot function comes in here
