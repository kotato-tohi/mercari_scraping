from selenium import webdriver
import chromedriver_binary
import time
import csv
import os
import datetime

export_path = "./../data/get_mercari/"
columns = "date,ave,max,min\n"

file = open('./../data/kind/master.csv')
reader = csv.reader(file)
header = next(reader)
browser = webdriver.Chrome()
words = []

dt_now = datetime.datetime.now()
date = (dt_now.strftime('%Y/%m/%d'))
print (date)

## create target list
for row in reader:
    if row[2] == "1":
        word = row[0][:-1] + "_" + row[1]
        words.append(word)


urls = {}
sum = 0
cnt = 0
max = 0
min = 99999999

## init url list
for word in words:
    url = "https://www.mercari.com/jp/search/?sort_order=created_desc&keyword="+ word +"&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max=&status_on_sale=1"
    urls[word] = url



for search in urls:
    if os.path.exists(export_path+search+".csv") == False:
        f = open(export_path+search+".csv", 'w')
        f.write(columns)
       
    else:
        f = open(export_path+search+".csv", 'a')
     
    time.sleep(3)
    browser.get(urls[search])
    posts = browser.find_elements_by_css_selector(".items-box")
   
    for post in posts:
        title=post.find_element_by_css_selector("h3.items-box-name").text
        if "土" in title:
            continue

        if "チップ" in title:
            continue
        
        price=post.find_element_by_css_selector(".items-box-price").text
        int_price = int(price[1:].replace(",",""))

        if min > int_price:
            min = int_price
            min_title = title
        
        if max < int_price:
            max = int_price
            max_titel = title
            
        sum = sum + int_price
        cnt +=1
        print (title,":",price)
    ave = round(sum/cnt,1)
    row = str(date)+","+str(ave)+","+str(max)+","+str(min)+"\n"
    f.write(row)
        

print ("min_title", min_title)
print ("min:",min)
print ("max:",max)
print ("max_title:",max_titel)
print ("ave:",ave)



browser.close()
f.close()