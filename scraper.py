import requests
from bs4 import BeautifulSoup

# URL de la web que queremos scrapear
url = "https://www.elmundo.es/"

# Hacer la solicitud HTTP a la web
response = requests.get(url)

# Verificar que la respuesta es correcta (200 OK)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Buscar los títulos de las noticias
    noticias = soup.find_all("h2")[:10]  # Extraemos los 10 primeros titulares

    # Imprimir los títulos en consola
    print("Noticias destacadas de El Mundo:")
    for noticia in noticias:
        print("-", noticia.text.strip())

else:
    print("Error al acceder a la web")
