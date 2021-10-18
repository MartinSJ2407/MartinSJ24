from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import selenium 

url = f"https://carros.mercadolibre.com.do/autos-camionetas/2020/_NoIndex_True"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

page_text1 = doc.find_all(class_="ui-search-item__title ui-search-item__group__element")

nombres = list()

for i in page_text1:
	nombres.append(i.text)
print(nombres)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver  = webdriver.Chrome(PATH)

driver.get("https://carros.mercadolibre.com.do/autos-camionetas/2020/_NoIndex_True")

# Extract lists of "buyers" and "prices" based on xpath.
buyers = driver.find_elements_by_xpath('//a[@class="Siguiente"]')[0].click







# url1 = f"https://carros.mercadolibre.com.do/autos-camionetas/2020/_Desde_49_NoIndex_True"
# result1 = requests.get(url1).text
# doc1 = BeautifulSoup(result1, "html.parser")

# page_text1 = doc1.find_all(class_="ui-search-item__title ui-search-item__group__element")
# nombres1 = list()

# for i1 in page_text1:
# 	nombres1.append(i1.text)
# print(nombres1)

# url2 = f"https://carros.mercadolibre.com.do/autos-camionetas/2020/_Desde_97_NoIndex_True"
# result2 = requests.get(url2).text
# doc2 = BeautifulSoup(result2, "html.parser")

# page_text2 = doc2.find_all(class_="ui-search-item__title ui-search-item__group__element")

# nombres2 = list()

# for i2 in page_text2:
# 	nombres2.append(i2.text)
# print(nombres2)

# url3 = f"https://carros.mercadolibre.com.do/autos-camionetas/2020/_Desde_145_NoIndex_True"
# result3 = requests.get(url3).text
# doc3 = BeautifulSoup(result3, "html.parser")

# page_text3 = doc3.find_all(class_="ui-search-item__title ui-search-item__group__element")

# nombres3 = list()

# for i3 in page_text3:
# 	nombres3.append(i3.text)
# print(nombres3)

# url4 = f"https://carros.mercadolibre.com.do/autos-camionetas/2020/_Desde_193_NoIndex_True"
# result4 = requests.get(url4).text
# doc4 = BeautifulSoup(result4, "html.parser")

# page_text4 = doc4.find_all(class_="ui-search-item__title ui-search-item__group__element")

# nombres4 = list()

# for i4 in page_text4:
# 	nombres4.append(i4.text)
# print(nombres4)

# url5 = f"https://carros.mercadolibre.com.do/autos-camionetas/2020/_Desde_241_NoIndex_True"
# result5 = requests.get(url5).text
# doc5 = BeautifulSoup(result5, "html.parser")

# page_text5 = doc5.find_all(class_="ui-search-item__title ui-search-item__group__element")

# nombres5 = list()

# for i5 in page_text5:
# 	nombres5.append(i5.text)
# print(nombres5)