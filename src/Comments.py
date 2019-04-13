import os
import requests
import csv
import argparse
import re
import math
import builtwith
import sys
import string
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup

class comments_scrapping:
	def __init__(self, hotel_id,nom_hotel):
		self.llista_comentaris=[]
		self.llista_categories_comentaris=[]
		self.nom_hotel=nom_hotel
		self.hotel_id=hotel_id
		self.iteracio=1
		
	def scrap_page_comments(self,url):
		r = requests.get(url)
		#r.encoding = 'ISO-8859-1'
		#Obtenim el contingut del request
		soup = BeautifulSoup(r.content,features="lxml")
		lista_comentarios=soup.find_all('li', {'class': ['review_item clearfix']})
		if lista_comentarios==[]:
			raise ValueError('No hi ha mes comentaris')
		else:
			index_comentari=1
			for comentario in lista_comentarios:
				fecha=comentario.find('meta', {'itemprop': ['datePublished']})["content"]
				contenedor_coment=comentario.find('div', {'class': ['review_item_review']})
			# #for datos in lista_comentarios:
			# #print(lista_comentarios[1])
				#provoquem un errror si no hih a llista de revisions (pagina es activa)
				#caracteristicas=contenedor_coment.find('ul', {'class':['review_item_info_tags']}).findChildren()
			# #print(caracteristicas)
				#Agafem la nota que està en aquest span
				nota=contenedor_coment.find('span', {'class': ['review-score-badge']}).text.replace('\n','')
				#Agafem comentaris positius negatious
				try:
					review_pos=contenedor_coment.find('p', {'class': ['review_pos']}).text.replace('\n','')
				except:
					review_pos=""
				try:
					review_neg=contenedor_coment.find('p', {'class': ['review_neg']}).text.replace('\n','')
				except:
					review_neg=""
				#Guardem informació general comentari
				self.llista_comentaris.append([self.hotel_id,self.iteracio,index_comentari,self.nom_hotel,nota,review_pos,review_neg,fecha])

				#Agafem tot els fills ul,(<li>) que descriuen les característiques de qui ha posat el comentari
				caracteristicas=contenedor_coment.find('ul', {'class':['review_item_info_tags']}).findChildren()
				for item in caracteristicas:
					element=item.text
					if element!='•':
						self.llista_categories_comentaris.append([self.hotel_id,self.iteracio,index_comentari,element.replace('\n','').replace('•','').replace(' ','')])
				#seguent comentari
				
				index_comentari=index_comentari+1
				
	def inicia_scrapring(self,url):
		try:
			r = requests.get(url)
			self.scrap_page_comments(url)
			max_pag=2
			self.iteracio=1
			print('Recollint comentaris: Iteració ' + str(self.iteracio) + ' de ' + self.nom_hotel )
			self.iteracio=2
			#Hem vist que la url de l pagina es aquesta i es mou en funció d'un parámetre 'url. Hem d'extreure de la pàgina normal el màxim de paginacions disponibles
			while self.iteracio<max_pag+1:
				paginacio="?label=gen173nr-1DCA0oRkIHcGluYW1hckgKWARoRogBAZgBCrgBF8gBDNgBA-gBAfgBAogCAagCA7gCmtDD5QXAAgE;sid=ab4245efa6cd9b489d059e8c37a9f987;customer_type=total;hp_nav=0;old_page=0;order=featuredreviews;page=" + str(self.iteracio) + ";r_lang=es;rows=75&amp;"
				try:
					#Provem de fer el request
					#print(url+paginacio)
					r = requests.get(url+paginacio)
					self.scrap_page_comments(url+paginacio)
					print('Recollint comentaris: Iteració ' + str(self.iteracio) + ' de ' + self.nom_hotel )
					max_pag=max_pag+1
					self.iteracio=self.iteracio+1
					
				except:
					max_pag=0
				
		except:
			print('No hi ha comentaris disponibles per '+ self.nom_hotel )
	




