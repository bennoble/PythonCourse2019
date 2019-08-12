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
import unicodedata

# Loading main faculty tree page
web_address = 'https://polisci.wustl.edu/people/88/'
web_page = urllib.request.urlopen(web_address)
web_page

# Parsing faculty tree
parsed_page = BeautifulSoup(web_page.read())
parsed_page

# Save every a tag with the class card
all_a_tags = parsed_page.find_all('a', {'class' : "card"})

# For every faculty member's a entry, add the main polisci website url + the
# href link to the faculty's personal page
personal_pages = []
for i in range(len(all_a_tags)):
  personal_pages.append("https://polisci.wustl.edu" + all_a_tags[i]['href'])

# Take all the individual faculty URLs and parse them. Save them to a list.
parsed_pages = []
for i in range(len(personal_pages)):
  try:
    parsed_pages.append(BeautifulSoup(urllib.request.urlopen(personal_pages[i]).read()))  
  except urllib.error.URLError:
    pass
  
names = []
title = []
special = []

# For all the parsed individual pages, collect the names, titles, and specializations.
# Append them to specific lists.
for i in range(len(parsed_pages)):
  names.append(parsed_pages[i].find('h1').get_text()) 
  title.append(parsed_pages[i].find('div', {'class' : "title"}).get_text())
  special.append(parsed_pages[i].find('div', {"class" : "post-excerpt"}).get_text())

# Fix coding errors on special
special2 = []
for i in range(len(special)):
  special2.append(unicodedata.normalize('NFKD', special[i]))

# Parse all faculty pages for a tags
parsed_a = []  
for i in range(len(parsed_pages)):
  parsed_a.append(parsed_pages[i].find_all('a'))

# If faculty pages a tag includes "mailto" in the href, save it. It collects
# two different email addresses, however, the first email of each double entry 
# is what we want, so I save every other email.
email = []
for pages in range(len(parsed_a)):
  for items in parsed_a[pages]:
    if "mailto" in items['href']:
      email.append(items.get_text())
      
email = email[::2]

# Write the CSV file
with open('faculty.csv', 'w') as f:
  writer = csv.DictWriter(f, fieldnames = ("Name", "Title", "Email", "Specialization", "Personal Page"))
  writer.writeheader()
  for i in range(len(names)):
    writer.writerow({"Name" : names[i], "Title" : title[i], "Email" : email[i], "Specialization" : special2[i], "Personal Page" : personal_pages[i]})



# Below is all of my scratch paper that I wanted to save just in case

aksoy = urllib.request.urlopen(personal_pages[0])  
aksoy_parsed = BeautifulSoup(aksoy.read())
aksoy_parsed.find('h1')
aksoy_parsed.find('div', {'class' : "title"}).get_text()
a_a = aksoy_parsed.find_all('a')
a_a

for i in range(len(a_a)):
  if "mailto" in a_a[i]['href']:
    print(a_a[i].get_text())

a_links = aksoy_parsed.find('ul', {'class' : 'links'})
a_links.find('a')['href']

aksoy_parsed.find('div', {"class" : "post-excerpt"}).get_text()

personal_pages

parsed_pages = []
for i in range(len(personal_pages)):
  try:
    parsed_pages.append(BeautifulSoup(urllib.request.urlopen(personal_pages[i]).read()))  
  except urllib.error.URLError:
    pass
  
names = []
title = []
special = []

for i in range(len(parsed_pages)):
  names.append(parsed_pages[i].find('h1').get_text()) 
  title.append(parsed_pages[i].find('div', {'class' : "title"}).get_text())
  special.append(parsed_pages[i].find('div', {"class" : "post-excerpt"}).unicodedata.normalize('NFKD', parsed_pages[i].get_text())


for i in range(len(special)):
  unicodedata.normalize('NFKD', special[i])

  #  special[i].translate({ord('\n'): None})
  #if "\n" in special[i]:
    
special

parsed_a = []  
for i in range(len(parsed_pages)):
  parsed_a.append(parsed_pages[i].find_all('a'))

len(parsed_a)

email = []
for pages in range(len(parsed_a)):
  for items in parsed_a[pages]:
    if "mailto" in items['href']:
      email.append(items.get_text())
      
email = email[::2]

links = []
indiv_sites = []

for i in range(len(parsed_pages)):
  links.append(parsed_pages[i].find('ul', {'class' : 'links'}))

for i in range(len(links)):
  indiv_sites.append(links[i].find('a')['href'])
  

names
title
email
indiv_sites

for i in names:     
  print(i.get_text())
    
names[0:10]

links = []
indiv_sites = []

for i in range(len(parsed_pages)):
  links.append(parsed_pages[i].find('ul', {'class' : 'links'}))