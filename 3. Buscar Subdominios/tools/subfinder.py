import subprocess

def ejecutar_subfinder(dominio):
    try:
        print(f"Ejecutando subfinder para {dominio}")
        resultado = subprocess.run(['subfinder', '-d', dominio], capture_output=True, text=True)

        if resultado.returncode != 0:
            print(f"Error al ejecutar subfinder: {resultado.stderr}")
            return []

        # Si el comando se ejecutó correctamente, leemos el archivo con los resultados
        return resultado.stdout.splitlines()
    # Si el comando no se ejecutó correctamente, mostramos un mensaje de error
    except subprocess.CalledProcessError as e:
        print(e)

