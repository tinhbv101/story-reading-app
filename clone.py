import requests 
from bs4 import BeautifulSoup
import re

i = 1044
while(True):
    # if i > 50: break
    # https://metruyencv.com/truyen/dau-la-dai-luc-trung-sinh-duong-tam/chuong-1
    url = 'https://metruyencv.com/truyen/dau-la-dai-luc-trung-sinh-duong-tam/chuong-' + str(i)  # Replace this with the URL of the website you want to scrape
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        html_content = response.content
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        # Find all the text elements (e.g., paragraphs, headings, etc.) you want to scrape
        text_elements1 = soup.find("div", class_="h1 mb-4 font-weight-normal nh-read__title")
        title = text_elements1.get_text() + '\n\n'
        
        text_elements = soup.find("div", class_="c-c")
        # Extract the text from each element and concatenate them into a single string
        scraped_text = title + '\n\n' + ' '.join(element.get_text() for element in text_elements).replace("   ", "\n\n")
        print(title)
        f = open("dttt/" + str(i) + ".txt", "w")
        f.write(scraped_text)
        f.close()
        i = i + 1
    else:
        print("Failed to fetch the website: " + 1)
        break
exit()
