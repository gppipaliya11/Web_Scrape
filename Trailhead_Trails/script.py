from bs4 import BeautifulSoup
import requests
import pandas as pd

BASE_URL = r'https://trailhead.salesforce.com'
URL = r'https://trailhead.salesforce.com/en/trails'
req = requests.get(URL)
soup = BeautifulSoup(req.content, 'html.parser')

columns = ['Trail Name', 'Description', 'URL']
df = pd.DataFrame()

container_class = 'tiles-filterable tiles-container'
output_container = soup.find('div', {'class':container_class})

articles = output_container.find_all('article')
for article in articles:
    trialheadName = article.h3.a['title']
    page_url = BASE_URL + article.h3.a['href']
    description = article.find('div', {'class':'tile-description'}).text
    df = df.append({'Trial Name': trialheadName,
                    'Description': description,
                    'URL': page_url}, ignore_index=True)

df.to_csv('Trail Output.csv', index=False)
print('Export complete')
