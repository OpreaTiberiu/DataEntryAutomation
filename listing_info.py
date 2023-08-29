import requests
from bs4 import BeautifulSoup

URL = "https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov?id=82493726#&lon=26.128921508789066&lat=44.49405638181746&zoom=10"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7"
}


def get_listing_info():
    response = requests.get(
        URL,
        headers=HEADERS)
    response.raise_for_status()
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    gallery = soup.find("div", {"id": "container_anunturi_harta"})

    listings = gallery.find_all("div", {"class": "box-anunt"})

    info = []

    for listing in listings:
        if listing.find("p", {"class": "location_txt"}) is not None:
            info.append({
                "address": listing.find("p", {"class": "location_txt"}).find("span").text.strip(),
                "price": listing.find("span", {"class": "pret-mare"}).text.strip(),
                "link": listing["href"],
            })
    return info
