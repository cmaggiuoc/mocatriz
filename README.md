
# Repositori :mocatriz
# PRACTICA 1era Part
# Practica realizada per  : (THEMAGGICIANS) 
## Joan A. Maggi Gómez 
## Carles Maggi Gómez 
## Repositori per la  pràctica Tipologia i Ccicle de Vida de les Dades

## Instal·lació de paquets
Per instal·lar el pip3 actualitzat cal executar el programa  get-pip.py

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
L'scrip s'ha ejecutar de la següent manera : python main.py --nhotels 30


# Descripció de la Pràctica a realitzar
L'objectiu d'aquesta practica es  la creació d'un dataset a partir de les dades
contingudes en la web ***www.booking.com*** , concretament del hotels de Barcelona,
per tal de limitar la mida del resultats.
A partir del numero d'hotels demanats es crean aquest fitxers :

Consideracions.txt 	: Contingut de totes les dades relacionades amb el context
urls_xml.txt		: Urls dels sitemap, per si cal tractar-les més endevant.
nomdelfitxer.csv	: nomdelfitxer.csv on es guarden el resultats de la cerca en la web. 


# 1. Context.
## Consideracions
	En el fitxer de text consideracions.txt estan totes les dades relatives el context que envolta
	aquest url.
	Com a dades més significatives tenin :
		**Propietari** : {  "domain_name": [    "BOOKING.COM",    "booking.com"  ], "registrar": "MarkMonitor, Inc.", ....}
		**Grandaria**  : Aproximadamente 53.400.000 resultados
		**Tecnologia** : {'web-servers': ['Nginx'], 'javascript-frameworks': ['Prototype', 'RequireJS', 'jQuery']}
		**Robots.txt** : El contingut del fitxer estar dins del fitxer consideracions.txt
		**Sitema***    : El contingut del sitemap està dins del fixer robots.txt, però hem fet un fitxer
						a part on nomes hi ha les urls del fitxers .xml per si cal tractar-les després.	


#2. Definir un títol pel dataset. Triar un títol que sigui descriptiu.
#3. Descripció del dataset. Desenvolupar una descripció breu del conjunt de dades
que s'ha extret (és necessari que aquesta descripció tingui sentit amb el títol
triat).
#4. Representació gràfica. Presentar una imatge o esquema que identifiqui el
dataset visualment
#5. Contingut. Explicar els camps que inclou el dataset, el període de temps de les
dades i com s'ha recollit.
#6. Agraïments. Presentar el propietari del conjunt de dades. És necessari incloure
cites de recerca o anàlisis anteriors (si n'hi ha).
#7. Inspiració. Explicar per què és interessant aquest conjunt de dades i quines
preguntes es pretenen respondre.
#8. Llicència. Seleccionar una d'aquestes llicències pel dataset resultant i explicar
#el motiu de la seva selecció:
○ Released Under CC0: Public Domain License
○ Released Under CC BY-NC-SA 4.0 License
○ Released Under CC BY-SA 4.0 License
○ Database released under Open Database License, individual contents
under Database Contents License
○ Other (specified above)
○ Unknown License
#9. Codi. Adjuntar el codi amb el qual s'ha generat el dataset, preferiblement en
#Python o, alternativament, en R.
#10. Dataset. Presentar el dataset en format CSV







## main.py





