import requests
from bs4 import BeautifulSoup

# URLs de las noticias generales y la sección de deportes
url_general = "https://www.elmundo.es/"
url_sport = "https://www.elmundo.es/deportes.html"

# Función para extraer noticias con imágenes
def obtener_noticias(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        noticias = soup.find_all("article")[:10]  # Extraemos los 10 primeros artículos
        resultado = []
        for noticia in noticias:
            titulo_tag = noticia.find("h2")
            enlace_tag = noticia.find("a", href=True)
            imagen_tag = noticia.find("img")

            if titulo_tag and enlace_tag:
                titulo = titulo_tag.text.strip()
                enlace = enlace_tag["href"]

                # Asegurar que el enlace es completo
                if not enlace.startswith("http"):
                    enlace = "https://www.elmundo.es" + enlace

                # Obtener la URL de la imagen (si existe)
                imagen = imagen_tag["src"] if imagen_tag else "https://via.placeholder.com/150"

                resultado.append({"titulo": titulo, "enlace": enlace, "imagen": imagen})
        return resultado
    return []

# Obtener noticias de cada sección
lista_noticias = obtener_noticias(url_general)
lista_noticias_sport = obtener_noticias(url_sport)

# Mostrar los resultados en consola
print("\nNoticias destacadas de El Mundo:")
for noticia in lista_noticias:
    print(f"- {noticia['titulo']} ({noticia['enlace']}) - Imagen: {noticia['imagen']}")

print("\nNoticias destacadas de la sección Sport:")
for noticia in lista_noticias_sport:
    print(f"- {noticia['titulo']} ({noticia['enlace']}) - Imagen: {noticia['imagen']}")
