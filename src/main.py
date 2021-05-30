from selenium import webdriver
import chromedriver_binary
import time




browser = webdriver.Chrome()
word = ["エケベリア", "不夜城", "ブルーバニーカクタス"]
url = "https://www.mercari.com/jp/search/?sort_order=created_desc&keyword="+ word +"&category_root=&brand_name=&brand_id=&size_group=&price_min=&price_max=&status_on_sale=1"
time.sleep(3)

posts = browser.find_elements_by_css_selector(".items-box")
time.sleep(1)
sum = 0
cnt = 0
max = 0
min = 99999999



browser.get(url)

for post in posts:
    title=post.find_element_by_css_selector("h3.items-box-name").text
    
    ## exclude 
    if "土" in title:
        continue

    ##########


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



ave = round(sum/cnt,1)

print ("min_title", min_title)
print ("min:",min)
print ("max:",max)
print ("max_title:",max_titel)
print ("ave:",ave)

browser.close()