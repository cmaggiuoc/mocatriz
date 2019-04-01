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


