import re
import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'
response = requests.get(url)
raw_html = response.text

parsed_html = BeautifulSoup(raw_html, 'html.parser')

# print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#top-3 > div > div > div')
# print(top_jobs_heading.text)

div = top_jobs_heading.parent

for p in div.select('p'):
    print(re.sub(r'\s{1,}', ' ', p.text).strip())
