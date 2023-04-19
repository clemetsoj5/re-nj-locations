import requests
from bs4 import BeautifulSoup
from csv import writer

#Pulls website
response = requests.get('http://www.city-data.com/crime/crime-New-Jersey.html')
response2 = requests.get('http://www.city-data.com/crime/crime-New-Jersey2.html')

#Creates a soup instance to scrape
soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

# Finds the unordered lists(ul) titled 'index' within each website
# This is the ul that holds all of the information
ul = soup.find('ul', attrs={'class': 'index'})
ul2 = soup2.find('ul', attrs={'class': 'index'})

# Finds individual elements of the ul, the html link for each town
# Create a list, use it in the for loop, push, and then print outside
link_list = []
for li in ul.find_all('li'):
        links = li.find('a')['href']
        link_list.append(links)

for li2 in ul2.find_all('li'):
        links2 = li2.find('a')['href']
        link_list.append(links2)

link_list = ['http://www.city-data.com/crime/' + x for x in link_list]