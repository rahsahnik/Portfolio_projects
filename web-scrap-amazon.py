import csv
import requests
from bs4 import BeautifulSoup 

def req(page):
    header= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
            "Accept-Encoding":"gzip, deflate", 
               "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
               "DNT":"1",
               "Connection":"close", 
               "Upgrade-Insecure-Requests":"1"}
    url='https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011&page='+str(page)       
    response=requests.get(url, headers=header)
    
    return response

def scrap_items(item):
    # Name, description, URL
    
    atag=item.h2.a
    name=atag.text.split('|')[0].strip()
    description=atag.text.strip()
    url='https://amazon.com'+atag.get('href')
    
    try:
        # Price 
        temp=item.find('span','a-price')
        price=temp.find('span','a-offscreen').text
        # OriginalPrice
        temp=item.find('span' ,{'class':'a-price a-text-price'})
        original=temp.find('span',{'class':'a-offscreen'}).text
    except AttributeError:
        return
    
    try:
        # rating
        rating =item.i.text[:3]

        #no of people rated
        temp=item.find('span',{'class':'a-size-base s-underline-text'})
        voters=temp.text
        
        # discount
        temp=item.find('div',{'class':'a-row a-size-base a-color-base'})
        discount=temp.a.span.text.strip('-')
        
    except AttributeError:  # If no rating or votes set it to empty
        rating=''
        voters=''
                
    
    result=(name,description,price,rating,voters,discount,original,url)
    
    return(result)

# Scrapping the first N pages , here we are doing for first 10 pages.

records=[]
for page in range(1,11):
    resp=req(page)
    soup=BeautifulSoup(resp.content, 'html.parser')
    product_name=soup.find_all('div',{'data-component-type':'s-search-result'})
    for item in product_name:
        record=scrap_items(item)
        if record:
            records.append(record)
            
with open('web-scarp.csv','w',newline='',encoding='utf-8') as fp:
    writer=csv.writer(fp)
    writer.writerow(['Product-Name','Description','Price','Rating','People-Reviewed','Discount','Original-Price','Product-URL'])
    writer.writerows(records)            
