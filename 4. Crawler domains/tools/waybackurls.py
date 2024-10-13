import subprocess

def limpiar_dominio(dominio):
    """Quitar http:// y https:// de un dominio."""
    return dominio.replace("http://", "").replace("https://", "")

def ejecutar_waybackurls(domain):
    """Ejecuta Waybackurls en un dominio y captura la salida"""
    try:
        # Limpiar el dominio antes de ejecutarlo
        dominio_limpio = limpiar_dominio(domain)

        print(f"Ejecutando Waybackurls para {dominio_limpio}")

        # Ejecutar el comando de Waybackurls
        resultado = subprocess.run(
            ["waybackurls", dominio_limpio], 
            capture_output=True, 
            text=True, 
            check=True
        )

        # Si hay un error, imprimirlo y devolver una lista vacía
        if resultado.returncode != 0:
            print(f"Error al ejecutar Waybackurls: {resultado.stderr}")
            return []

        # Separar las líneas de la salida y devolverlas
        urls = resultado.stdout.splitlines()
        return [url for url in urls if url.strip()]

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar Waybackurls: {e.stderr}")
        return []
    
    except FileNotFoundError:
        print("Waybackurls no está instalado o no se encontró en el PATH.")
        return []
