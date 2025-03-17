import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def scrape_noticias(request):
    # URLs de las noticias generales y la sección de deportes
    url_general = "https://www.elmundo.es/"
    url_sport = "https://www.elmundo.es/deportes.html"

    def obtener_noticias(url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            noticias = soup.find_all("article")[:10]
            resultado = []
            for noticia in noticias:
                titulo_tag = noticia.find("h2")
                enlace_tag = noticia.find("a", href=True)
                imagen_tag = noticia.find("img")

                if titulo_tag and enlace_tag:
                    titulo = titulo_tag.text.strip()
                    enlace = enlace_tag["href"]

                    if not enlace.startswith("http"):
                        enlace = "https://www.elmundo.es" + enlace

                    # Verificar si la etiqueta <img> existe y tiene el atributo 'src'
                    imagen = imagen_tag["src"] if imagen_tag and imagen_tag.has_attr("src") else "https://via.placeholder.com/150"

                    resultado.append({"titulo": titulo, "enlace": enlace, "imagen": imagen})
            return resultado
        return []

    lista_noticias = obtener_noticias(url_general)
    lista_noticias_sport = obtener_noticias(url_sport)

    return render(request, "scraper/noticias.html", {"noticias": lista_noticias, "noticias_sport": lista_noticias_sport})
