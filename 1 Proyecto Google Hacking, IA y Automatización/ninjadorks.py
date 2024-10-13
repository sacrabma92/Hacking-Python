from dotenv import load_dotenv, set_key  # Libreria que ayuda a crear las variables de entorno
from result_parser import ResultParser
from file_downloader import FileDownloader
import os   # Libreria que nos ayuda a interactuar con el OS
from googlesearch import GoogleSearch
import argparse    # Libreria que nos ayudara a pasar argumentos por linea de comandos
import sys

def env_config():
    """Configurar el archivo .env con los valores proporcionados"""
    api_key = input("Introduce tu API KEY de Google: ")
    engine_id = input("Introduce el ID del buscador personalziado de Google: ")
    set_key(".env", "API_KEY_GOOGLE", api_key)
    set_key(".env", "SEARCH_ENGINE_ID", engine_id)


def main(query, configure_env, start_page, pages, lang, output_json, output_html, downloads):
    # Comprobamos si existe el ficher .env
    env_exists = os.path.exists(".env")

    # En caso que el archivo .env no existra realizar lo siguiente
    if not env_exists or configure_env:
        env_config()
        print("Archivo .env configurado satisfactoriamente.")
        sys.exit(1)

    #Cargamos las variables en el entorno
    load_dotenv()

    # Leer la clave API(max. 100 peticions /dia)
    API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")

    # Leer el identificador del buscador
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

    if not query:
        print("Indica una consulta con el comando -q. Utilzia el comando -h para mostrar la ayuda.")
        sys.exit(1)

    # Instanciamos el objeto
    gsearch = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)
    resultados = gsearch.search(query, 
                                start_page=start_page,
                                pages=pages,
                                lang=lang)

    rparser = ResultParser(resultados)

    # Mostrar los resultados en linea de consola de comandos
    rparser.mostrar_pantalla()

    if output_html:
        rparser.exportar_html(output_html)
    
    if output_json:
        rparser.exportar_json(output_json)

    if downloads:
        #Separar las extension de los archivos en una lista
        file_types = downloads.split(",")
        # Nos quedamos unicamente con los URLs de los resultados obtenidos
        urls = [resultado['link'] for resultado in resultados]
        fdownloader = FileDownloader("Descargas")
        fdownloader.filtrar_descargar_archivos(urls, file_types)

# Ejecutamos el programa
if __name__ == "__main__":
    # Configuración de los argumentos del programa  
    parser = argparse.ArgumentParser(description="Esta herramienta permite realziar Hacking con buscadores de manera automatica")
    parser.add_argument("-q","--query", type=str, 
                        help="Especifica el dork que desea buscar.\nEjemplo: -q \"pass\" \"usuario\" filetype:sql")
    parser.add_argument("-c", "--configure", action="store_true",
                        help="Inicia el proceso de configuracion del archivo .env. \nUtiliza esta opcion sin otros argumentos para configurar las claves.")
    parser.add_argument("--start-page", type=int, default=1,
                        help="Define la pagina de inicio del buscador para obtener los resultados.")
    parser.add_argument("--pages", type=int, default=1,
                        help="Numero de paginas de resultados de busqueda.")
    parser.add_argument("--lang", type=str, default="lang_es",
                        help="Codigo de idioma para los resultados de busqueda. Por defecto es 'lang_es' español.")
    parser.add_argument("--json", type=str,
                        help="Exporta los resultados en formato JSON en el fichero especificado.")
    parser.add_argument("--html", type=str,
                        help="Exporta los resultados a formato HTML en el fichero especificado.")
    parser.add_argument("--download", type=str, default="all",
                        help="Especifica las extensiones de los archivos que quieres descargar entre coma. Ej: --download 'pdf,doc,sql'")
    # Almacenar los argumentos que le enviemos
    args = parser.parse_args()

    main(query=args.query,
         configure_env=args.configure,
         pages=args.pages,
         start_page=args.start_page,
         lang=args.lang,
         output_html=args.html,
         output_json=args.json,
         downloads=args.download)
    