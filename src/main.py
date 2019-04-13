import os
import requests
import csv
import argparse
import re
import math
import builtwith
import whois
import sys
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup
from Hotels import hotels_scrapping
import pandas as pd


print('Avaluem el robots.txt')
## Avaluem el robots.txt ##
page=requests.get("https://www.booking.com/robots.txt")
if page.status_code == 200:
	souprob = BeautifulSoup(page.content,'html.parser')
	robottxt= souprob.prettify()
#Guardem les dades en un fitxer de text
	r = open ('consideracions.txt','w')
	r.write(robottxt)
	r.close()
else:
	print ("Error en la URL")
	sys.exit()

print('Guardem informació de Sitemap')
## Guardo las urls del xml del sitema en el fitxer"
urls_xml = open ('urls.txt','w')
text=souprob.text
soupsite_raw= (souprob.text).split("\n")
fin =len(soupsite_raw)
for i in  range(0,fin):
	if soupsite_raw[i][:7]=="Sitemap":
		if range == fin:
			urls_xml.write(soupsite_raw[i][9:])
		else:
			urls_xml.write(soupsite_raw[i][9:] + '\n')

urls_xml.close()

print('Baixem la informació de la tecnologia')
## Tecnologia ##
tecnologia = builtwith.builtwith('https://www.booking.com')

#Guardem les dades en un fitxer de text

r = open('consideracions.txt','a')
r.write('\n' + 'Tecnologia : ' )
r.write(str(tecnologia))
r.close()

print('Baixem la informació respecte grandaria del conjunt del domini')
## Grandaria ###
url ="https://www.google.es/search?source=hp&ei=wrqjXICQOsyblwTw6avgAw&q=site%3Awww.booking.com&btnK=Buscar+con+Google&oq=site%3Awww.booking.com&gs_l=psy-ab.3...3527.8692..9067...0.0..0.55.978.20......0....1..gws-wiz.....0..0i131j0j0i3j0i10.h2_32y7cUoo"

page=requests.get(url)
soup = BeautifulSoup(page.content,features="lxml")
tamany=soup.find(id="resultStats")

#Guardem les dades en un fitxer de text 
r = open('consideracions.txt','a')
r.write('\n' + 'Grandaria : ' )
r.write(tamany.string)
r.close()

## Propietari de la pàgina ##
print('Baixem la informació de dades del propietari')

#Guardem les dades del propietari en un fitxer de text 
r = open('consideracions.txt','a')
r.write('\n' + 'Propietari : ' )
r.write(str((whois.whois)('https://www.booking.com')))
r.close()

print('Baixem la informació dels hotels de Barcelona de booking i els seus comentaris')
#Preguntem per entrada el nombre d'hotels, en múltiples de 15 
parser = argparse.ArgumentParser()
parser.add_argument("--nhotels", help="Introdueix el nombre d'hotels de bcn a escrapear (mínim 15)")
args = parser.parse_args()
if args.nhotels is None:
	nhotels=0.0
else:
	nhotels=float(args.nhotels)	

scrapt_booking=hotels_scrapping(nhotels)
sisapUrl="https://www.booking.com/searchresults.es.html?label=gen173nr-1DCAsoRjiLA0gzWARoRogBAZgBCrgBF8gBDNgBA-gBAfgBAogCAagCA7gC0NvZ5AXAAgE;sid=bed493c85d8693a2b7074f734f20b8fc;closed_msg=584507;dest_id=-372490;dest_type=city;hlrd=14&"
scrapt_booking.inicia_scrapring(sisapUrl)

with open('HotelsBarcelonaBooking.csv','w',newline='') as f:
	writer = csv.writer(f)
	writer.writerows(scrapt_booking.llista_hotels)
f.close()

#Convertim a datafame per problemes d'encoding de la categorització de comentario.
df = pd.DataFrame(scrapt_booking.llista_comentaris)
df.to_csv('ComentarisXHotelsBarcelonaBooking.csv', index=False, header=False)

#Convertim a datafame per problemes d'encoding de la categorització de comentario.
df = pd.DataFrame(scrapt_booking.llista_categoria_comentaris)
df.to_csv('CategoriesXComentariBooking.csv', index=False, header=False)
