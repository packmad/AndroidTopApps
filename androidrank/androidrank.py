import requests
from bs4 import BeautifulSoup


def generate_file(sort_mode: int = 0):
    for i in range(1, 10001, 20):
        url = "https://www.androidrank.org/listcategory?category=&start={}&sort={}&price=free&hl=en".format(i, sort_mode)
        print(url)
        req = requests.get(url)
        if req.status_code != 200:
            print("Problem! Request status code: ", req.status_code)
            break
        soup = BeautifulSoup(req.text, "lxml")
        with open("./output/topAppsByRatings.txt", 'a') as out_file:
            for a in soup.find_all('a', href=True):
                href = a["href"]
                if href.startswith("/application/"):
                    packname = href.split("/")[-1].replace("?hl=en","").strip()
                    out_file.write(packname + "\n")
            out_file.flush()
