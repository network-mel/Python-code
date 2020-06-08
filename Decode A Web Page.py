# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re

if __name__ == "__main__":
    url = "http://www.nytimes.com"
    r = requests.get(url)
    r_html = r.text
    with open("parsing_out.txt", "w") as f_out:
        soup = BeautifulSoup(r_html, features="html.parser")
        titles = soup.find_all("article" , class_="css-8atqhb") 
        for title in titles:
            f_out.write(title.text + "\n")
            print(title.text)
