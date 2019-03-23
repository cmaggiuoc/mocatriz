import os
import requests
import csv
import argparse
from datetime import datetime
from datetime import timedelta
from bs4 import BeautifulSoup

sisapUrl="https://booking.com/hotel/es/barcelona"
r = requests.get(sisapUrl)
print(r.content)
fitxer=open("c:/Users/carle/booking.txt","w")
data = r.text.encode('utf-8')

fitxer.write(data)
soup = BeautifulSoup(r.content)
soup.find_all("a", class_="hotel_name_link url")
