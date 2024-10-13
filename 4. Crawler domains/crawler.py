import argparse
from utils.file_utils import leer_dominios, guardar_resultado
from tools.katana import ejecutar_katana
from tools.waybackurls import ejecutar_waybackurls

# Función para verificar si la entrada es un archivo o un dominio único
def verificar_entrada(entrada):
    if entrada.endswith(".txt"):
        # Leer archivo de dominios
        dominios = leer_dominios(entrada)
    else:
        # Si no es un archivo, asumir que es un dominio
        dominios = [entrada]

    urls_totales = set()

    # Procesar cada dominio y obtener las URLs
    for dominio in dominios:
        print(f"Procesando {dominio}...")

        # Ejecutar Katana y agregar URLs
        urls_katana = ejecutar_katana(dominio)
        urls_totales.update(urls_katana)

        # Ejecutar Waybackurls y agregar URLs
        urls_wayback = ejecutar_waybackurls(dominio)
        urls_totales.update(urls_wayback)

    # Guardar los resultados si se encontraron URLs
    if urls_totales:
        guardar_resultado(urls_totales, "domains_crawled.txt")
    else:
        print("No se encontraron URLs para guardar.")

# Función principal para manejar los argumentos
def main():
    parser = argparse.ArgumentParser(description="Crawler de subdominios con Katana")
    
    # Argumentos para el dominio o la lista de dominios
    parser.add_argument("-d", "--domain", type=str, help="Dominio único Ej: facebook.com")
    parser.add_argument("-l", "--list", type=str, help="Archivo de dominios .txt")
    
    # Parsear los argumentos
    args = parser.parse_args()

    # Verificar si se pasa un dominio o una lista de dominios
    if args.domain:
        verificar_entrada(args.domain)
    elif args.list:
        verificar_entrada(args.list)
    else:
        print("Debes proporcionar un dominio con '-d' o una lista de dominios con '-l'.")

if __name__ == "__main__":
    main()
