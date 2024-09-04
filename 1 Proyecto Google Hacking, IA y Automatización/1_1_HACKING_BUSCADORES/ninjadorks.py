from dotenv import load_dotenv
import os
from googlesearch import GoogleSearch

def main():
    #Cargamos las variables en el entorno
    load_dotenv()

    # Leer la clave API(max. 100 peticions /dia)
    API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")

    # Leer el identificador del buscador
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")


    query = '"pass" "usuario" filetype:sql' #cadena a buscar

    # Instanciamos el objeto
    gsearch = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)
    resultados = gsearch.search(query, pages=2)
    print(resultados)

if __name__ == "__main__":
    main