from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import math
from flask import request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
app = Flask(__name__)
CORS(app)


def parse_page1(s,p,t):
    page_items=[]
    url="https://megamarket.ru/catalog/cnc/#?q="+s+"&store=352670"+f"&page={p}"
    if p==1:
        url="https://megamarket.ru/catalog/cnc/#?q="+s+"&store=352670"
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'catalog-items-list'))
    )
    catalog=driver.find_element(By.CLASS_NAME, 'catalog-items-list')
    products = driver.find_elements(By.XPATH, "//div[@data-test='product-item']")
    for product in products:
        try:
            img = product.find_element(By.XPATH, ".//img[@data-test='product-image']").get_attribute('src')
            name = product.find_element(By.XPATH, ".//a[@data-test='product-name-link']").text
            price = product.find_element(By.XPATH, ".//span[@data-test='product-price']").text
            price=int((re.search(r'\d+',price).group()))
        
            page_items.append({
            't': t,
            'i': img,
            'n': name,
            'c': price
        })
        except Exception as e:
            print(f"Error parsing product: {e}")
    driver.quit()
    return page_items
        
@app.route('/parse/vkysvill', methods=['POST'])
def parse_url1():
    res=[]
    data = request.json
    string = data['input']
    count = data['count']
    print(string, "\n", count)
    url="https://megamarket.ru/catalog/cnc/#?q="+string+"&store=352670"

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div/div[1]/div[2]/div/div/div/h1'))
    )
    total=driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[1]/div[2]/div/div/div/h1' ).text
    driver.quit()
    total=int(re.search(r'\d+', total).group())
    pagesToParse=min(math.ceil(int(count)/24), math.ceil(total/7))
    if pagesToParse==0:
        badRes={}
        badRes['i']= ''
        badRes['min']= 0
        badRes['max']= 0
        badRes['t']= 0
        badRes['n']="Ничего не найдено"
        badRes['srp']=0
        badRes['c']=0
    else:
        for i in range (1,pagesToParse+1):
            res+=parse_page1(string, i, total)
        srp=0
        minn=100000
        maxx=-10
        for i in res:
            srp+=int(i['c'])
            minn=min(int(i['c']),minn)
            maxx=max(int(i['c']),maxx)

        srp//=len(res)
        for i in res:
            i['srp']=srp
            i['min']=minn
            i['max']=maxx
        return jsonify(res[:int(count)])



def parse_page2(s,p,t):
    page_items=[]
    url="https://megamarket.ru/catalog/cnc/#?q="+s+"&store=274218"+f"&page={p}"
    if p==1:
        url="https://megamarket.ru/catalog/cnc/#?q="+s+"&store=274218"
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'catalog-items-list'))
    )
    catalog=driver.find_element(By.CLASS_NAME, 'catalog-items-list')
    products = driver.find_elements(By.XPATH, "//div[@data-test='product-item']")
    for product in products:
        try:
            img = product.find_element(By.XPATH, ".//img[@data-test='product-image']").get_attribute('src')
            name = product.find_element(By.XPATH, ".//a[@data-test='product-name-link']").text
            price = product.find_element(By.XPATH, ".//span[@data-test='product-price']").text
            price=int((re.search(r'\d+',price).group()))
        
            page_items.append({
            't': t,
            'i': img,
            'n': name,
            'c': price
        })
        except Exception as e:
            print(f"Error parsing product: {e}")
    driver.quit()
    return page_items


@app.route('/parse/globus', methods=['POST'])
def parse_url2():
    res=[]
    data = request.json
    string = data['input']
    count = data['count']
    print(string, "\n", count)
    url="https://megamarket.ru/catalog/cnc/#?q="+string+"&store=274218"

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div/div[1]/div[2]/div/div/div/h1'))
    )
    total=driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[1]/div[2]/div/div/div/h1' ).text
    driver.quit()
    total=int(re.search(r'\d+', total).group())
    pagesToParse=min(math.ceil(int(count)/24), math.ceil(total/7))
    print(pagesToParse)
    for i in range (1,pagesToParse+1):
        res+=parse_page2(string, i, total)
    srp=0
    minn=100000
    maxx=-10
    for i in res:
        srp+=int(i['c'])
        minn=min(int(i['c']),minn)
        maxx=max(int(i['c']),maxx)

    srp//=len(res)
    for i in res:
        i['srp']=srp
        i['min']=minn
        i['max']=maxx
    return jsonify(res[:int(count)])




def parse_page3(s,p,t):
    page_items=[]
    url="https://megamarket.ru/catalog/cnc/#?q="+s+"&store=274282"+f"&page={p}"
    if p==1:
        url="https://megamarket.ru/catalog/cnc/#?q="+s+"&store=274282"
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'catalog-items-list'))
    )
    catalog=driver.find_element(By.CLASS_NAME, 'catalog-items-list')
    products = driver.find_elements(By.XPATH, "//div[@data-test='product-item']")
    for product in products:
        try:
            img = product.find_element(By.XPATH, ".//img[@data-test='product-image']").get_attribute('src')
            name = product.find_element(By.XPATH, ".//a[@data-test='product-name-link']").text
            price = product.find_element(By.XPATH, ".//span[@data-test='product-price']").text
            price=int((re.search(r'\d+',price).group()))
        
            page_items.append({
            't': t,
            'i': img,
            'n': name,
            'c': price
        })
        except Exception as e:
            print(f"Error parsing product: {e}")
    driver.quit()
    return page_items
        
@app.route('/parse/lenta', methods=['POST'])
def parse_url3():
    res=[]
    data = request.json
    string = data['input']
    count = data['count']
    print(string, "\n", count)
    url="https://megamarket.ru/catalog/cnc/#?q="+string+"&store=274282"

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div/div[1]/div[2]/div/div/div/h1'))
    )
    total=driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[1]/div[2]/div/div/div/h1' ).text
    driver.quit()
    total=int(re.search(r'\d+', total).group())
    pagesToParse=min(math.ceil(int(count)/24), math.ceil(total/7))
    print(pagesToParse)
    for i in range (1,pagesToParse+1):
        res+=parse_page3(string, i, total)
    srp=0
    minn=100000
    maxx=-10
    for i in res:
        srp+=int(i['c'])
        minn=min(int(i['c']),minn)
        maxx=max(int(i['c']),maxx)

    srp//=len(res)
    for i in res:
        i['srp']=srp
        i['min']=minn
        i['max']=maxx
    return jsonify(res[:int(count)])


def parse_page4(s,p,t):
    page_items=[]
    url="https://megamarket.ru/catalog/cnc/#?q="+s+"&store=253543"+f"&page={p}"
    if p==1:
        url="https://megamarket.ru/catalog/cnc/#?q="+s+"&store=253543"
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'catalog-items-list'))
    )
    catalog=driver.find_element(By.CLASS_NAME, 'catalog-items-list')
    products = driver.find_elements(By.XPATH, "//div[@data-test='product-item']")
    for product in products:
        try:
            img = product.find_element(By.XPATH, ".//img[@data-test='product-image']").get_attribute('src')
            name = product.find_element(By.XPATH, ".//a[@data-test='product-name-link']").text
            price = product.find_element(By.XPATH, ".//span[@data-test='product-price']").text
            price=int((re.search(r'\d+',price).group()))
        
            page_items.append({
            't': t,
            'i': img,
            'n': name,
            'c': price
        })
        except Exception as e:
            print(f"Error parsing product: {e}")
    driver.quit()
    return page_items
        
@app.route('/parse/metro', methods=['POST'])
def parse_url4():
    res=[]
    data = request.json
    string = data['input']
    count = data['count']
    print(string, "\n", count)
    url="https://megamarket.ru/catalog/cnc/#?q="+string+"&store=253543"

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div/div[1]/div[2]/div/div/div/h1'))
    )
    total=driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[1]/div[2]/div/div/div/h1' ).text
    driver.quit()
    total=int(re.search(r'\d+', total).group())
    pagesToParse=min(math.ceil(int(count)/24), math.ceil(total/7))
    print(pagesToParse)
    for i in range (1,pagesToParse+1):
        res+=parse_page4(string, i, total)
    srp=0
    minn=100000
    maxx=-10
    for i in res:
        srp+=int(i['c'])
        minn=min(int(i['c']),minn)
        maxx=max(int(i['c']),maxx)

    srp//=len(res)
    for i in res:
        i['srp']=srp
        i['min']=minn
        i['max']=maxx
    return jsonify(res[:int(count)])



def parse_page5(s,p,t):
    page_items=[]
    url="https://megamarket.ru/catalog/cnc/#?q="+s+"&store=361364"+f"&page={p}"
    if p==1:
        url="https://megamarket.ru/catalog/cnc/#?q="+s+"&store=361364"
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'catalog-items-list'))
    )
    catalog=driver.find_element(By.CLASS_NAME, 'catalog-items-list')
    products = driver.find_elements(By.XPATH, "//div[@data-test='product-item']")
    for product in products:
        try:
            img = product.find_element(By.XPATH, ".//img[@data-test='product-image']").get_attribute('src')
            name = product.find_element(By.XPATH, ".//a[@data-test='product-name-link']").text
            price = product.find_element(By.XPATH, ".//span[@data-test='product-price']").text
            price=int((re.search(r'\d+',price).group()))
        
            page_items.append({
            't': t,
            'i': img,
            'n': name,
            'c': price
        })
        except Exception as e:
            print(f"Error parsing product: {e}")
    driver.quit()
    return page_items
        
@app.route('/parse/paterochka', methods=['POST'])
def parse_url5():
    res=[]
    data = request.json
    string = data['input']
    count = data['count']
    print(string, "\n", count)
    url="https://megamarket.ru/catalog/cnc/#?q="+string+"&store=361364"

    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/main/div/div[1]/div[2]/div/div/div/h1'))
    )
    total=driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[1]/div[2]/div/div/div/h1' ).text
    driver.quit()
    total=int(re.search(r'\d+', total).group())
    pagesToParse=min(math.ceil(int(count)/24), math.ceil(total/7))
    print(pagesToParse)
    for i in range (1,pagesToParse+1):
        res+=parse_page5(string, i, total)
    srp=0
    minn=100000
    maxx=-10
    for i in res:
        srp+=int(i['c'])
        minn=min(int(i['c']),minn)
        maxx=max(int(i['c']),maxx)

    srp//=len(res)
    for i in res:
        i['srp']=srp
        i['min']=minn
        i['max']=maxx
    return jsonify(res[:int(count)])



if __name__ == "__main__":
    app.run()

