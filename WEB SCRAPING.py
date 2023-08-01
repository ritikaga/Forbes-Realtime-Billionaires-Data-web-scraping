import pandas as pd

# import the python request library to query a website
import requests

# specify the url we want to scrape from

link="https://ceoworld.biz/2023/03/04/the-worlds-richest-people-top-billionaires-2023/"

#convert the web page to text

link_text = requests.get(link).text
print(link_text)

#import BautifulSoup library to pull data out of HTML and XML files
from bs4 import BeautifulSoup

#convert Link_text into a BeautifulSoup Object
soup = BeautifulSoup(link_text, 'html.parser')
print(soup)

# make the indentation proper
print(soup.prettify())

# take a look at the title of the web page
print(soup.title)

#Only the string not the tags
print(soup.title.string)


#Fetch all the table tags
all_table = soup.find('table')
print(all_table)

#fetch all the table tags with class name="wikitable sortable"
table=soup.find_all('table')
print(table)

first_table = soup.find('table',class_='tablepress tablepress-id-620 tablepress-responsive')
print(first_table)

table_titles=first_table.find_all('th')
print(table_titles)

world_table_titles = [title.text.strip() for title in table_titles]
print(world_table_titles)

#Convert the list into a dataframe 
df = pd.DataFrame(columns = world_table_titles)
print(df)

#put the title into a list 
column_data = first_table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = individual_row_data

print(df)
print(df.head(50))

# save the data into an csv file 
df.to_csv(r'C:\Users\ritik\OneDrive\Documents\project data analysis\Python project\Web Scarping\World_Billionare_2023.csv', index = False)
