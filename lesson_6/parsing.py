from bs4 import BeautifulSoup
import requests

def parsing_barmak():
    response = requests.get(url="https://www.nbkr.kg/index.jsp?lang=RUS")
    soup = BeautifulSoup(response.text, 'lxml')

    course = soup.find_all('table', class_="table table-striped")

    for title in course:
        print(title)
        print(f"{title.text}")



parsing_barmak()