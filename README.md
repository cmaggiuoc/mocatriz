# Repositori :mocatriz
# PRACTICA 1era Part
# Practica realizada per  : Joan A. Maggi Gómez i Carles Maggi Gómez (THEMAGGICIANS)
## Repositori per la  pràctica Tipologia i Ccicle de Vida de les Dades

# Descripció de la Pràctica a realitzar
L'objectiu d'aquesta practica es  la creació d'un dataset a partir de les dades
contingudes en la web ***www.booking.com*** , concretament del hotels de Barcelona,
per tal de limitar la mida del resultats.


#1. Context. Explicar en quin context s'ha recol·lectat la informació. Explicar per
què el lloc web triat proporciona aquesta informació.
## Consideracions
	En el fitxer de text consideracions.txt estan totes les dades relatives el context que envolta
	aquest url.
	Com a dades més significatives tenin :
		***Propietari*** : {  "domain_name": [    "BOOKING.COM",    "booking.com"  ], "registrar": "MarkMonitor, Inc.", ....}
		***Grandaria***  : Aproximadamente 53.400.000 resultados
		***Tecnologia*** : {'web-servers': ['Nginx'], 'javascript-frameworks': ['Prototype', 'RequireJS', 'jQuery']}
		***Robots.txt*** : El contingut del fitxer estar dins del fitxer consideracions.txt
		***Sitema***     : El contingut del sitemap està dins del fixer robots.txt, però hem fet un fitxer
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

## Instal·lació de paquets
Per instal·lar el pip3 actualitzat cal executar el programa  get-pip.py


Per ejecutar l'script cal instal·lar aquest paquets 

```
pip3 install pandas
pip3 install requests
pip3 install lxml
pip3 install beautifulsoup4
pip3 install builtwith
```

L'scrip s'ha ejecutar de la següent manera :
```

python main.py --nhotels 30

```

Actualment no fa res.


