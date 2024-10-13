import subprocess

def ejecutar_katana(domain):
    try:
        # Ejecutamos katana y guardamos el resultado en un archivo
        print(f"Ejecutando katana para {domain}")
        # Ejecutamos katana y guardamos el resultado en un archivo
        resultado = subprocess.run(["katana", "-u", domain, "-d 5 -ps -pss waybackarchive,commoncrawl,alienvalut -kf -jc -fx -ef woff,css,png,svg,jpg,woff2,jpeg,gif,svg"], capture_output=True, text=True)

        # Si el comando no se ejecutó correctamente, mostrar mensaje de error
        if resultado.returncode != 0:
            print(f"Error al ejecutar katana: {resultado.stderr}")
            # Si el comando se ejecutó correctamente, retornar las urls encontradas
        return resultado.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar katana: {e}")
        return ""