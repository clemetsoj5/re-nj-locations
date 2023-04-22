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

def open_city_page(link_list):
    with open('crimeData.csv','w') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['City','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
        csv_writer.writerow(headers)