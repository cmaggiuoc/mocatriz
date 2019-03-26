import os
import requests
import csv
import argparse
import re
import math
import builtwith
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup


## Avaluem el robots.txt

page=requests.get("https://www.booking.com/robots.txt")
if page.status_code == 200:
	souprob = BeautifulSoup(page.content)
	robottxt= souprob.prettify()
	print(robottxt)

else:
	print ("Error en la URL")


### Mirem quina tecnologia fa servir el lloc

tecnologia = builtwith.builtwith('https://www.booking.com')

print(tecnologia)




#CCrida request a la pagina on hi ha els hotels de Barcelona 
sisapUrl="https://www.booking.com/searchresults.es.html?label=gen173nr-1DCAsoRjiLA0gzWARoRogBAZgBCrgBF8gBDNgBA-gBAfgBAogCAagCA7gC0NvZ5AXAAgE;sid=bed493c85d8693a2b7074f734f20b8fc;closed_msg=584507;dest_id=-372490;dest_type=city;hlrd=14&"
r = requests.get(sisapUrl)

#Obtenim el contingut del request
soup = BeautifulSoup(r.content,features="lxml")

#Agafem tots els links que tenen un hotel name
aux=soup.find('h2', class_='sorth1').text.replace(".","")
print(aux)

try:
    m = int(re.findall('\d+', aux)[0])
except AttributeError:
    # AAA, ZZZ not found in the original string
    m = '' # apply your error handling
print(m)
all_links = []
links = soup.find_all('a', {'class': ['hotel_name_link', '']})
for link in links:
	all_links.append('https://www.booking.com' + link.get('href').split(";")[0].replace('\n',''))
print(all_links)

#cada página dona 15 hotels, paginació serà m/15
max_pag=math.ceil(m/15)

for i in range(2, max_pag, 1):
#Per cada pagina del index, fem un request per obtenir tots els links dels hotels.
	url='https://www.booking.com/searchresults.es.html?aid=304142&amp;label=gen173nr-1FCAsoRjiLA0gzWARoRogBAZgBCrgBF8gBDNgBAegBAfgBAogCAagCA7gC0NvZ5AXAAgE&amp;sid=ab4245efa6cd9b489d059e8c37a9f987&amp;tmpl=searchresults&amp;class_interval=1&amp;closed_msg=584507&amp;dest_id=-372490&amp;dest_type=city&amp;hlrd=14&amp;label_click=undef&amp;raw_dest_type=city&amp;room1=A%2CA&amp;sb_price_type=total&amp;shw_aparth=1&amp;slp_r_match=0&amp;srpvid=ce588cee120e039a&amp;ssb=empty&amp;rows='+ str(i*15)
	r = requests.get(url)
	print ('Iteració' + str(i))
	#Obtenim el contingut del request
	soup = BeautifulSoup(r.content,features="lxml")
	links = soup.find_all('a', {'class': ['hotel_name_link', '']})
for link in links:
	all_links.append('https://www.booking.com' + link.get('href').split(";")[0].replace('\n',''))
	print (all_links)
