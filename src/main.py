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



## Avaluem el robots.txt ##

page=requests.get("https://wwww.booking.com/robots.txt")
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

## Tecnologia ##

tecnologia = builtwith.builtwith('https://www.booking.com')

#Guardem les dades en un fitxer de text

r = open('consideracions.txt','a')
r.write('\n' + 'Tecnologia : ' )
r.write(str(tecnologia))
r.close()

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

#Guardem les dades del propietari en un fitxer de text 
r = open('consideracions.txt','a')
r.write('\n' + 'Propietari : ' )
r.write(str((whois.whois)('https://www.booking.com')))
r.close()


#Preguntem per entrada el nombre d'hotels, en múltiples de 15 
parser = argparse.ArgumentParser()
parser.add_argument("--nhotels", help="Introdueix el nombre d'hotels de bcn a escrapear (mínim 15)")
args = parser.parse_args()

#Crida request a la pagina on hi ha els hotels de Barcelona 
sisapUrl="https://www.booking.com/searchresults.es.html?label=gen173nr-1DCAsoRjiLA0gzWARoRogBAZgBCrgBF8gBDNgBA-gBAfgBAogCAagCA7gC0NvZ5AXAAgE;sid=bed493c85d8693a2b7074f734f20b8fc;closed_msg=584507;dest_id=-372490;dest_type=city;hlrd=14&"
r = requests.get(sisapUrl)

#Obtenim el contingut del request
soup = BeautifulSoup(r.content,features="lxml")

#Agafem el divs dels hotels
all_links = []
div=soup.find_all('div', {'class': ['sr_item','sr_item_new','sr_item_default','sr_property_block','sr_flex_layout','sr_item_no_dates']})
for div_hotel in div:
	#Creem el vector de l'hotel
	hotel_id=div_hotel['data-hotelid']
	hotel_stars=div_hotel['data-class']
	hotel_puntuacio=div_hotel['data-score']
	link = div_hotel.find('a', {'class': ['hotel_name_link', 'url']})
	url_hotel='https://www.booking.com' + link.get('href').split(";")[0].replace('\n','')
	hotel_name=link.find('span',class_='sr-hotel__name').text.replace('\n','')
	
	#Anem a buscar la pàgina de l'hotel per adquirir les propietats de les facilities
	r= requests.get(url_hotel)
	soup2 = BeautifulSoup(r.content,features="lxml")
	links = soup2.find_all('div',{'class': 'facilitiesChecklistSection'})
	print("Definint propietat de l'hotel "+ hotel_name)
	
	#Per cada facilitie l'afegim al nostre array 
	for item in links:
		propietat=item.find('h5').text.strip()
		elem = [x.text for x in item.find_all('li')]
		for valor in elem:
			print("Propietat " + valor.replace('\n','').strip() + " de " + hotel_name )
			all_links.append([hotel_id,hotel_stars,hotel_puntuacio,hotel_name,url_hotel,propietat,valor.replace('\n','').strip()])

#Busquem dins la paginació l'offset més gran. Veiem per url que offset es un parametre que s'afegeix a la url (offset*15)
iter=soup.find_all('a', {'class': ['bui-pagination__link sr_pagination_link']})
#Preparem per afagar la paginació més gran
if args.nhotels=="":
	max_pag=0
	for link in iter:
		if max_pag<int(link.string) :
			max_pag=int(link.string)
else:
	max_pag=int(float(args.nhotels)/15)-1

#Iterem fins al nombre màxim de pàgines, modificant la URL amb el valor d'offset que toqui (arriba fins (max_pag-1)*15)
for i in range(1, max_pag+1, 1):
	#Per cada pagina del index, fem un request per obtenir tots els links dels hotels.
	url='https://www.booking.com/searchresults.es.html?aid=304142&amp;label=gen173nr-1FCAsoRjiLA0gzWARoRogBAZgBCrgBF8gBDNgBAegBAfgBAogCAagCA7gC0NvZ5AXAAgE&amp;sid=ab4245efa6cd9b489d059e8c37a9f987&amp;tmpl=searchresults&amp;class_interval=1&amp;closed_msg=584507&amp;dest_id=-372490&amp;dest_type=city&amp;hlrd=14&amp;label_click=undef&amp;raw_dest_type=city&amp;room1=A%2CA&amp;sb_price_type=total&amp;shw_aparth=1&amp;slp_r_match=0&amp;srpvid=ce588cee120e039a&amp;ssb=empty&amp;rows=15&offset='+ str(i*15)
	r = requests.get(url)
	soup = BeautifulSoup(r.content,features="lxml")
	
	#Agafem els divs dels hotels
	div=soup.find_all('div', {'class': ['sr_item','sr_item_new','sr_item_default','sr_property_block','sr_flex_layout','sr_item_no_dates']})
	for div_hotel in div:
		#Creem el vetor de l'hotel
		hotel_id=div_hotel['data-hotelid']
		hotel_stars=div_hotel['data-class']
		hotel_puntuacio=div_hotel['data-score']
		link = div_hotel.find('a', {'class': ['hotel_name_link', 'url']})
		url_hotel='https://www.booking.com' + link.get('href').split(";")[0].replace('\n','')
		hotel_name=link.find('span',class_='sr-hotel__name').text.replace('\n','')
		
		#Anem a buscar la pàgina de l'hotel per adquirir les propietats de les facilities
		r= requests.get(url_hotel)
		soup2 = BeautifulSoup(r.content,features="lxml")
		links = soup2.find_all('div',{'class': 'facilitiesChecklistSection'})
		print("Definint propietat de l'hotel "+ hotel_name)

		#Per cada facilitie l'afegim al nostre array 
		for item in links:
			propietat=item.find('h5').text.strip()
			elem = [x.text for x in item.find_all('li')]
			for valor in elem:
				print("Propietat " + valor.replace('\n','').strip() + " de " + hotel_name )
				all_links.append([hotel_id,hotel_stars,hotel_puntuacio,hotel_name,url_hotel,propietat,valor.replace('\n','').strip()])
		
	
#Escribim el resultat
with open('out.csv','w',newline='') as f:
	writer = csv.writer(f)
	writer.writerows(all_links)
f.close()
