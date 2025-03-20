# import requests
# from bs4 import BeautifulSoup

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import pandas as pd

# channel_url = 'https://www.youtube.com/@lbwcreations7414/videos'
# response = requests.get(channel_url)
# soup = BeautifulSoup(response.content, 'html.parser')

# video_elements = soup.find_all('h3', class_='yt-lockup-title')

# video_titles = []



# for video in video_elements:
#     title = video.a.text
#     video_titles.append(title)

# for title in video_titles:
#     print(title)



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
driver = webdriver.Chrome('C:/Users/likhi/Downloads/chromedriver.exe')