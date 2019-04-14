# Pràctica de Tipologia i Cicle de Vida de les Dades
1era Part
## Autors
***Carles Maggi Gómez***   
***Joan A. Maggi Gómez***  
*THEMAGGICIANS* 
## Repositori per la  pràctica
mocatriz 
## Programari utilitzat
Python 3.7 64 Bits
## SO
Windows 10 64 Bits
## Instal·lació de paquets
Per instal·lar el pip3 actualitzat cal executar el programa get-pip.py
```
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
```
L'scrip pot scrapejar tots els hotels o bé es por limitar a un nombre d'hotels (mútiple de 15 per la paginació de Booking).  
La sintaxis es'ha ejecutar de la següent manera : python main.py --nhotels numero_hotels

## Estructura

A la carpeta [src](https://github.com/cmaggiuoc/mocatriz/tree/master/src) trobem els fitxers de codi font:  
**main.py**(https://github.com/cmaggiuoc/mocatriz/tree/master/src/main.py) arxiu principal a que es crida per començar scraping python main.py --nhotels numero_hotels  
**Hotels.py**(https://github.com/cmaggiuoc/mocatriz/tree/master/src/Hotels.py) classe per scrapejar els Hotels, a través d'un link fix de cerca (i paginació)  
**Comments.py**(https://github.com/cmaggiuoc/mocatriz/tree/master/src/Comments.py) classe per scrapejar els comentaris, a través d'un link de sitemap amb una estructura determinada (i paginació)

A la carpeta [CSV](https://github.com/cmaggiuoc/mocatriz/tree/master/CSV) trobem els fitxers csv sortida del scraping.  
A la carpeta [FitxersContext](https://github.com/cmaggiuoc/mocatriz/tree/master/FitxersContext) trobem els fitxers generats en l'extració de robots, sitemap, whois, etc..  
A la carpeta [recursos](https://github.com/cmaggiuoc/mocatriz/tree/master/recursos) trobem els recursos imatges, o codi python per actualitzar a la versió 3.  

# Descripció de la Pràctica a realitzar
L'objectiu d'aquesta practica és la creació d'un dataset a partir de les dades
contingudes en un enllaç de la web ***www.booking.com*** , concretament del hotels de Barcelona,
per tal de limitar la mida del resultats.
## A partir del número d'hotels demanats es crean aquest fitxers 
### HotelsBarcelonaBooking.csv
Dataset que inclou la llista d'hotels trobats.
### ComentarisXHotelsBarcelonaBooking.csv
Dataset de comentaris per hotel de hotels.csv
### CategoriesXComentariBooking.csv
Categories assoacides a un comentari d'un hotel, una fila de comentaris.csv.
## També es crean aquest dos fitxers .txt amb la infomració sobre el contexte.
### Consideracions.txt 
Contingut de totes les dades relacionades amb el context.  
### urls.txt
Urls dels sitemap, per si cal tractar-les més endevant.


# 1. Context.
## Consideracions
En el fitxer de text consideracions.txt estan totes les dades relatives el context que envolta aquest url.  
Com a dades més significatives tenin :
### Propietari :
{  "domain_name": [    "BOOKING.COM",    "booking.com"  ], "registrar": "MarkMonitor, Inc.", ....}
### Grandaria  :
Aproximadamente 53.400.000 resultados
### Tecnologia :
{'web-servers': ['Nginx'], 'javascript-frameworks': ['Prototype', 'RequireJS', 'jQuery']}
### Robots.txt :
El contingut del fitxer estar dins del fitxer ***consideracions.txt***
### Sitemap    :
El contingut del sitemap està dins del fixer ***robots.txt***, però hem fet el fitxer ***urls_xml.txt*** a part  
on només hi ha les urls del fitxers '.xml' per si cal tractar-les després.	


# 2. Definir un títol pel dataset. Triar un títol que sigui descriptiu.

## HotelsBarcelonaBooking  
## ComentarisXHotelsBarcelonaBooking  
## CategoriesXComentariBooking

# 3. Descripció del dataset. Desenvolupar una descripció breu del conjunt de dades que s'ha extret (és necessari que aquesta descripció tingui sentit amb el títol triat).
Hem creat 3 datasets donada la informació que consideravem interessant descarregar i la naturalessa de la mateixa  
conceptualment hem creat el dataset de HotelsBarcelonaBooking el dataset ComentarisXHotelsBarcelonaBooking que extreu  
tots els comentaris que hem trobat i finalment el Dataset CategoriesXComentariBooking que obté la categorització per  
cadasqun dels comentaris. 

# 4. Representació gràfica. Presentar una imatge o esquema que identifiqui el dataset visualment



![Consultar GraficExplicatiu.png](/recursos/GraficExplicatiuDataset.png "Gràfic explicatiu Dataset")

# 5. Contingut. Explicar els camps que inclou el dataset, el període de temps de les dades i com s'ha recollit.

Agafem a partir d'un enllaç de búsqueda genèric (sense referència temporal) el conjunt de hotels de barcelona,  
i d'aquí recollim el conjunt de comentaris que estan vinculats a aquest hotels accesibles (creiem que no  
tots els publicats són accesibles) i per cada comentari agafem les categories que el categoritzem i creem un  
fitxer per tal d'establir un "model relacional" entre datasets

## HotelsBarcelonaBooking

IdHotel		: *BigInt* que identifica de manera únivoca el hotel
Estrelles	: *Int* Número d'estrelles, en cas que n'hi hagi  
Nota		: *Float* Nota promig de l'hotel  
Nom			: *String* Nom de l'hotel  
Link		: *String* Url de la página de l'hotel  

## ComentarisXHotelsBarcelonaBooking

IdHotel				: *BigInt*	Identifica de manera únivoca el hotel  
IdIteració			: *Int* 	Primera part que identifica un comentari (iteració llista comentaris)  
Index				: *Int*		Segon part d'identificació de comentari (número de comentari dins la iteració)   
NomHotel			: *String*	Nom de l'hotel    
Nota				: *Float*	Nota que otorga el comentari de l'hotel   
Comentari Postiu	: *Text* 	Comentari positiu si n'hi ha
Comentari Negatiu	: *Text* 	Comentari negatiu si n'hi ha  
Data Comentari		: *Date* 	Data enregistrada del comentari  

## CategoriesXComentariBooking

Un comentari pot estar categoritzat per una o més categories.

IdHotel		: *BigInt*	Identifica de manera únivoca el hotel  
IdIteració	: *Int* 	Primera part que identifica un comentari (iteració llista comentaris)  
Index		: *Int* 	Segon part d'identificació de comentari (número de comentari dins la iteració)  
Categoria	: *Text*  	Categoria  amb la que s'ha categoritzat el comentari   
 

# 6. Agraïments. Presentar el propietari del conjunt de dades. És necessari incloure cites de recerca o anàlisis anteriors (si n'hi ha).

Agraim a Booking.com poder scrapejar aquests datasets

# 7. Inspiració. Explicar per què és interessant aquest conjunt de dades i quines preguntes es pretenen respondre.

Farem una explicació en funció de les persones que poden tenir un interés respecte l'activitat comercial en qüestió

**Propietari hotel**: Poder fer un seguiment, planificant un scraping diari, de com evoluciona la nota del seu hotel i la de les seus competidors.  
**Client Hotel**	: Comparar en funció de la categorització dels comentaris aquells hotels que tinguin una millor nota.

# 8. Llicència. Seleccionar una d'aquestes llicències pel dataset resultant i explicar el motiu de la seva selecció:

Triem la llicència ***Released Under CC0: Public Domain License*** perquè   
de la mateixa manera que nosaltres hem obtingut les dades en obert, nosaltres pensem  
que pot ser útil per a tercers

# 9. Codi. Adjuntar el codi amb el qual s'ha generat el dataset, preferiblement en Python o, alternativament, en R.
En el directori src podem trobar el codi generat :  
**Main.py**		: Programa principal amb un paràmetre. Cal ejecutarlo : main.py --nhotels 30  
**Comments**	: Classe que recull i guarda els comentaris al dataset *ComentarisXHotelsBarcelonaBooking*  
**Hotels**		: Classe que recull i guarda les dades genèriques de l'Hotel   

# 10. Dataset. Presentar el dataset en format CSV

En el directori csv podrem trobar els tres datasets :  

**HotelsBarcelonaBooking**  
**CategoriesXComentariBooking.csv**  
**ComentarisXHotelsBarcelonaBooking.csv**








