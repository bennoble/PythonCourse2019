## Go to https://polisci.wustl.edu/people/88/
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page
	
from bs4 import BeautifulSoup
import urllib.request
import csv 

web_address = 'https://polisci.wustl.edu/people/88/'
web_page = urllib.request.urlopen(web_address)
web_page

parsed_page = BeautifulSoup(web_page.read())
parsed_page
			
all_a_tags = soup.find_all('a', {'class' : "card"})
all_a_tags
all_a_tags[57]['class']	== ['card']			

personal_pages = []


for i in all_a_tags:
  if i["class"] == 'card':
    print(all_a_tags[i])
