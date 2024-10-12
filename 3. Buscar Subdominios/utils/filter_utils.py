import re

def filtrar_subdominios(salida):
    """Filtrar subdominios válidos usando una expresión regular."""
    # Expresión regular para validar subdominios
    regex = re.compile(r'^(?!-)([a-zA-Z0-9-]{1,63}(?<!-)\.)+[a-zA-Z]{2,}$')
    subdominios_validos = [linea for linea in salida.splitlines() if regex.match(linea)]
    return subdominios_validos