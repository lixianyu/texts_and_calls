import requests
from bs4 import BeautifulSoup

#theurl = ''https://en.wikipedia.org/wiki/Film_leader''
#theurl = 'https://en.wikipedia.org/wiki/Film'
#theurl = 'https://en.wikipedia.org/wiki/Projection_screen'
#theurl = 'https://en.wikipedia.org/wiki/Image_projector'
#theurl = 'https://en.wikipedia.org/wiki/Projector'
#theurl = 'https://en.wikipedia.org/wiki/Optical'
theurl = 'https://en.wikipedia.org/wiki/Physics'
#theurl = 'https://en.wikipedia.org/wiki/Flowering_plant'
#theurl = 'https://en.wikipedia.org/wiki/PICALM'

response = requests.get(theurl)
html = response.text
#print(html)
soup = BeautifulSoup(html, 'html.parser')
#print(soup.find(id='mw-content-text').p.a.get('href'))
#print(soup.find(id='mw-content-text').find(class_="mw-parser-output").p.a.get('href'))
'''
content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.a:
        print(element.a.parent.name)
        print(type(element.a.parent.name))
        if "sub" in element.a.parent.name:
            print("hahahahahah")
            continue
        else:
            first_relative_link = element.a.get('href')
            break
'''

content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
for element in content_div.find_all("p", recursive=False):
    if element.find("a", recursive=False):
        first_relative_link = element.find("a", recursive=False).get('href')
        break
print(first_relative_link)
