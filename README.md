# My History with Youtube
## DSA 210 2024-2045 Fall Term Project
You can review my project presentation slides by clicking [here](https://sabanciuniv-my.sharepoint.com/:p:/g/personal/yesim_tosun_sabanciuniv_edu/EY-4FDFpSzhNjPuiHCiYcS0B3_076Rs97N2J0sqR_oiqFw?e=THsrqX)
### Motivation 
In this project i wanted to a have a better comprehension of my internet usage over the time. Analysis of our data can provide us a collective idea about the person we are,
what we like, our interests, life goals and even our private information. With the internet data we can interpret the cause and effect relationships, correlations of events (such as the relation between years and my most watched categories) and finally have a reliable conclusion. Thus, i wanted to use my Youtube data and see how my interests, my frequency of usage or my purpose of watching videos have changed. 

### Data Sources
**I used Google takeout and the Youtube API to retrieve and process my data**
1. Google Takeout Data: This includes my 7 years of YouTube watch history, which allows for an in-depth exploration of my YouTube usage behavior over time. It will help identify patterns in interests, purpose of usage, and average watch time within this "time capsule" of data. 

2. YouTube API: This will provide additional insights, such as enhanced categorization and video details from my watch history, allowing for a more comprehensive understanding of the data and its patterns.

**The goal was to fetch the data in the areas and to analyze the topics below.**
1. Interest Over Time: By analyzing the watch history and search history datasets, we can identify and track the categories that reflect my interests during specific periods. This provides insights into how my interests have evolved over time.
2. Purpose of Usage: This categorization provides a broader perspective by grouping specific interests into general themes. It helps identify the main reasons for using YouTube, such as learning (e.g., educational videos), entertainment (e.g., music, comedy, or gaming), or productivity (e.g., tutorials or how-tos). By analyzing these generalized categories, we can draw meaningful conclusions about overall patterns of YouTube usage.
3. Frequency of Usage: The watch time data will be analyzed on a daily, monthly, and yearly basis to understand usage patterns and identify trends over different time periods.

### Data Processing
I fetched meta data of videos: video category, video watch date, video duration.​
Then created JSON Files for each year (e.g. 2017, 2018, …, 2024)​

### Data Analysis and Hypothesis Testing

You can find the visualized data of my YouTube history in the "Plots" folder or in my presentation slides, which include detailed analysis, explanations, and hypothesis testing using machine learning models.
For the analysis, I examined a 7-year dataset, focusing on:
1. Total number of videos in each category (all time)
2. Total duration of videos in each category (all time)
3. Total duration of videos watched each year (all time)
4. Yearly watched category durations
5. Monthly watched category durations

I then applied hypothesis testing to these models using techniques such as linear regression, t-tests, ANOVA F-statistics, and correlation matrix representation.
### Findings/Conclusion
#### The results of my data analysis:

-The total watched videos vary in terms of quantity and duration.​
**Most watched video categories by quantity (number of times):​**

1. People & Blogs - 24.6%​
2. Entertainment - 22.4%​
3. Music - 19.6%​

**Most watched video categories by duration:**

1. Gaming - 22.3%​
2. Entertainment - 18.4%​
3. Education - 13.6%​

-In my all-time watched categories, the "Gaming" category has the longest average video duration at 42 minutes. It is followed by "Sports" with an average of 20 minutes and "Education" with an average of 18 minutes.​

**By hypothesis testing I found out:​**

1. "My watch time has increased significantly over the years."​
2. "My watch durations are not significantly higher in summer."​
3. "I watched significantly more educational videos in 2022 while preparing for my university entry exam."​
4. "I watched gaming videos much more than ever in 2024."​

**Correlation Matrix Results:​**

-In year 2022, the categories generally do not correlate well with each other. But there is a strong correlation between categories "Music" and "Howto & Style" with positive correlation of 0.84. ​
-In 2024, there appear to be more negative correlations than positive ones. However, since these correlations are not strong, we cannot draw any definitive conclusions from them.   ​

### Limitations

1. YouTube's inability to categorize videos with the right accuracy.​
2. 
-Upon examining my raw data and the metadata of the videos, I noticed that the categorization was not entirely accurate. For instance, a concert video of a rock band might be categorized under "Entertainment" rather than "Music." Similarly, a guitar cover of a song is often categorized under "People & Blogs" or "How-to & Style" instead of "Music". ​
However the data is huge thus only thing I could do was to accept the results of the Youtube API data.​

3. The video durations retrieved through the YouTube API reflect the total length of the original videos, not the actual time spent watching them.​
4. 
-The issue arising from this limitation is that even if a user watches only 1 minute of an hour-long video, the data records the entire hour. Thus, I assumed for this project that I watched a significant proportion of each video I have watched.

### Future Work

Data can reveal an infinite amount of information about an individual. The possibilities for further analysis and hypothesis testing on this YouTube data are limitless. ​
At this point, it is difficult to stop discovering, as numerous scenarios and hypotheses come to mind for testing the data. In conclusion this project can evolve into different aspects of youtube usage and show many more interesting results in the future.​

**In this project, I used "All Time," "Yearly," and "Monthly" representations of my data due to its large size, spanning 7 years, which I wanted to explore comprehensively.​

**In the future, I could expand the analysis to include more granular forms, such as daily or hourly watch times.​

**With more detailed data, I would be able to conduct deeper analysis and draw more specific conclusions about my viewing behavior over time.​
