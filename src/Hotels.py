import os
import requests
import csv
import argparse
import re
import math
import builtwith
import sys
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup
from Comments import comments_scrapping
import json
import pandas as pd

class  hotels_scrapping:
	def __init__(self,nhotels):
		self.llista_hotels=[]
		self.llista_comentaris=[]
		self.llista_categoria_comentaris=[]
		self.nhotels=nhotels
		self.nnumhotels=0

	def scrap_page_hotels_comments(self,url):
		r = requests.get(url)
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
			#Afegim les propietats de l'hotel
			self.llista_hotels.append([hotel_id,hotel_stars,hotel_puntuacio,hotel_name,url_hotel])
			
			#Ara anem a buscar els comentaris per l'hotel
			match_url_comments=re.search('/.+',re.search('es/.+\?',url_hotel).group())
			url_comments="https://www.booking.com/reviews/es/hotel"+match_url_comments.group().replace('?','')
			self.nnumhotels=self.nnumhotels+1
			print('Hotel número ' + str(self.nnumhotels) + ': ' + hotel_name)
			comentari=comments_scrapping(hotel_id,hotel_name)
			comentari.inicia_scrapring(url_comments)
			if comentari.llista_comentaris!=[]:
				self.llista_comentaris=self.llista_comentaris+comentari.llista_comentaris
			if comentari.llista_categories_comentaris!=[]:
				#print(comentari.llista_categories_comentaris)
				self.llista_categoria_comentaris=self.llista_categoria_comentaris+comentari.llista_categories_comentaris
	
	def inicia_scrapring(self,url):
		try:
			
			#La primera URL es la que ens entra
			self.scrap_page_hotels_comments(url)
			#Preparem per afagar la paginació més gran
			if self.nhotels==0:
				#Hem d'anar a buscar paginació, per tnt, tornem a fer un request de la pagina
				r = requests.get(url)
				soup = BeautifulSoup(r.content,features="lxml")
				#Anem a paginar, per això requerim buscar dins la paginació l'offset més gran. Veiem per url que offset es un parametre que s'afegeix a la url (offset*15)
				iter=soup.find_all('a', {'class': ['bui-pagination__link sr_pagination_link']})
				max_pag=0
				for link in iter:
					if max_pag<int(link.string) :
						max_pag=int(link.string)
			else:
				max_pag=int((self.nhotels)/15)-1

			
			for i in range(1, max_pag+1, 1):
				url='https://www.booking.com/searchresults.es.html?aid=304142&amp;label=gen173nr-1FCAsoRjiLA0gzWARoRogBAZgBCrgBF8gBDNgBAegBAfgBAogCAagCA7gC0NvZ5AXAAgE&amp;sid=ab4245efa6cd9b489d059e8c37a9f987&amp;tmpl=searchresults&amp;class_interval=1&amp;closed_msg=584507&amp;dest_id=-372490&amp;dest_type=city&amp;hlrd=14&amp;label_click=undef&amp;raw_dest_type=city&amp;room1=A%2CA&amp;sb_price_type=total&amp;shw_aparth=1&amp;slp_r_match=0&amp;srpvid=ce588cee120e039a&amp;ssb=empty&amp;rows=15&offset='+ str(i*15)
				try:
					#Provem de fer el request
					r = requests.get(url)
					self.scrap_page_hotels_comments(url)
				except:
					print ('No podem seguir paginant')
				
		except:
			print('No hi ha hotels disponibles')





