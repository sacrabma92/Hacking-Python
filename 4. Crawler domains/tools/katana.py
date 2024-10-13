import subprocess

def ejecutar_katana(domain):
    """Ejecuta Katana en un dominio y captura la salida"""
    try:
        print(f"Ejecutando katana para {domain}")

        # Ejecutar el comando de Katana y capturar la salida
        resultado = subprocess.run(
                ["katana", 
                "-u", domain,  # Usar el dominio o archivo que se le pase
                "-d", "5",
                "-pss", "waybackarchive,commoncrawl,alienvalut",
                "-jc",
                "-ef", "woff,css,png,svg,jpg,woff2,jpeg,gif,svg"], 
            capture_output=True, 
            text=True, 
            check=True  # Si el comando falla, lanza una excepción
        )

        # Verificar si Katana no devolvió un error
        if resultado.returncode != 0:
            print(f"Error al ejecutar Katana: {resultado.stderr}")
            return []

        # Separar las líneas de la salida y devolverlas
        urls = resultado.stdout.splitlines()
        return [url for url in urls if url.strip()]

    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar Katana: {e.stderr}")
        return []
    
    except FileNotFoundError:
        print("Katana no está instalado o no se encontró en el PATH.")
        return []
