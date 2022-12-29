import  requests
from bs4 import BeautifulSoup as bs
import re
dept =input("enter dept")
name =input("Enter faculty name")
name =name.capitalize()

r =requests.get("https://www.cbit.ac.in/current_students/faculty-"+dept+"/")

webpage =bs(r.content ,features='html.parser')

links = webpage.select("div.current-students ul li a")

for link in links:
    if(link.find(string=re.compile(name))):
        url=link['href']
        break

print(url)

with open(f'{name}.pdf','wb') as pdf:
    facultypdf = pdf.write(requests.get(url).content)

