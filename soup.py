# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:59:56 2021

@author: Gonzalo
"""

import requests
from bs4 import BeautifulSoup
url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)


print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results_location = soup.find_all("p", class_="location")
results_title = soup.find_all("h2", class_="title is-5")


for result in results_location:
    print(result_location.text.strip())
    
for result in results_title:
    print(result.text.strip())