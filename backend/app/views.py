import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def scrape_noticias(request):
    url = "https://www.elmundo.es/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        noticias = soup.find_all("h2")[:10]  # Extraemos los 10 primeros titulares
        lista_noticias = [noticia.text.strip() for noticia in noticias]

        return render(request, "scraper/noticias.html", {"noticias": lista_noticias})
    else:
        return render(request, "scraper/error.html", {"error": "No se pudo acceder a la web."})
