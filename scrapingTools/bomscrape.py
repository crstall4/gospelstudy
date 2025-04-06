import requests, bs4, time
import pandas as pd

# Initialize an empty list to store the data
data = []

baseWebsite = 'https://www.churchofjesuschrist.org'
page = '/study/scriptures/bofm/introduction?lang=zhs'

for i in range(3):
    #time.sleep(3)
    res = requests.get(baseWebsite + page)
    print(page)
    res.raise_for_status()
    exampleSoup = bs4.BeautifulSoup(res.content, 'html.parser')

    # Scrape URL
    url = baseWebsite + page

    # Scrape book/chapter
    content_title_divs = exampleSoup.find_all('span', class_='contentTitle-JbPZw')
    location = content_title_divs[0].get_text(strip=True) if content_title_divs else "N/A"


    # Scrape contents
    contents_divs = exampleSoup.find_all('div', class_='body')
    contents = contents_divs[0].get_text(strip=True) if contents_divs else "N/A"

    #scrape contents 
    contents = exampleSoup.find_all('div', class_='body')[0]


    # Append the scraped data to the list
    data.append({'URL': url, 'LOCATION': location, 'CONTENTS': contents})

    # Check for the next page
    next_page = exampleSoup.select(".mobileNext-ARZIt")
    if next_page and next_page[0].attrs.get('href'):
        page = next_page[0].attrs.get('href')
    else:
        break

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('scraped_data.csv', index=False, encoding='utf-8')

print("Scraping completed. Data saved to 'scraped_data.csv'.")