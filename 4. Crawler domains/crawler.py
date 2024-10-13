import argparse
from utils.file_utils import leer_dominios, guardar_resultado
from tools.katana import ejecutar_katana

# Nombre del archivo de salida
NOMBRE_ARCHIVO_SALIDA = "domains_crawled.txt"

def verificar_entrada(entrada):
    # Verificar que la entrada sea un archivo o un dominio
    if entrada.endswith(".txt"):
        # Leer archivo de dominio
        dominios = leer_dominios(entrada)
    else:
        # Si no es un archivo, asumir que es un dominio
        dominios = [entrada]
    urls_totales = set()

    # Procesar cada dominio
    for dominio in dominios:
        print(f"Procesando {dominio}...")

        # Ejecutar herramientas y filtrar subdominios
        urls_crawler = ejecutar_katana(dominio)

        # Combinar urls validos en un solo archivo
        urls_totales.update(urls_crawler)
    
    # Guardar los resultados en un archivo
    guardar_resultado(urls_totales, NOMBRE_ARCHIVO_SALIDA)


def main(domain, list):

    # Configurar los argumentos programados
    if __name__ == "__main__":
        # Configurar los argumentos programados
        parser = argparse.ArgumentParser(description="Crawler de subdominios")
        parser.add_argument("-d", "--domain", type=str, 
                            help="Dominio Eje: facebook.com")
        parser.add_argument("-l", "--list", type=str, 
                            help="Archivo de dominios .txt")
    
    # Parsear los argumentos
    args = parser.parse_args()

        # Elegir la entrada correcta
    if args.dominio:
        verificar_entrada(args.domainio)
    else:
        verificar_entrada(args.archivo)

    main(domain = args.domain,
         list = args.list)
    
        