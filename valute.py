from urllib.request import urlopen
from xml.etree import ElementTree

r = urlopen("https://www.cbr.ru/scripts/XML_daily.asp")
rate = ElementTree.parse(r).findall('.//Valute/Name')
print(rate)
