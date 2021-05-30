from bs4.element import Tag
import requests
from bs4 import BeautifulSoup
import csv
export_path = "./../data/kind/master.csv"
url = "http://cactoloco.jp/dic/"
file = open('./../data/kind/kinds.csv')
reader = csv.reader(file)
header = next(reader)
dic_index = {}

f = open(export_path, 'w')
writer = csv.writer(f, lineterminator='\n')
column = "属性","品種","有効/無効"
writer.writerow(column)

for row in reader:
    dic_url = url + row[0]
    dic_index[row[1]] = dic_url

key_array = list(dic_index.keys())


for key in key_array:
    print (key)
    response = requests.get(dic_index[key])
    html = BeautifulSoup(response.content,'html.parser')

    names = html.select("dd a")
    print ("##############")
    print (key)
    print ("##############")

    for name in names:
        row = key,name.text,0
        writer.writerow(row)