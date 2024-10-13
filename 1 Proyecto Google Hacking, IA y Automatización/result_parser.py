import json
from rich.console import Console
from rich.table import Table


class ResultParser:
    """Forma en la cual se va a mostrar los datos ya sea en HTML o JSON"""
    def __init__(self, resultados):
        self.resultados = resultados

    def exportar_html(self, archivo_salida):
        """Metodo para crear la salida en formato HTML y crear el arhcivo .html"""
        # Abrimos la plantilla en formato lectura
        with open("html_template.html",'r', encoding='utf-8') as f:
            plantilla = f.read()
            
        elementos_html = '' # Variable que almacenara las etiquetas html 
        for indice, resultado in enumerate(self.resultados, start=1): # Creamos la estructura de la etiqueta HTML
            elemento = f'<div class="resultado">' \
                        f'<div class="indice">Resultado {indice}</div>' \
                        f'<h5>{resultado["title"]}</h5>' \
                        f'<p>{resultado["description"]}</p>' \
                        f'<a href="{resultado["link"]}" target="_blank">{resultado["link"]}</a>' \
                        f'</div>'
            elementos_html += elemento
        informe_html = plantilla.replace('{{ resultados }}', elementos_html) # Almacenamos en variable toda la estructura HTML creada
        with open(archivo_salida, 'w', encoding='utf-8') as f: # Escribimos en la plantilla todo lo almacenado
            f.write(informe_html)
        print(f"Resultados exportados a HTML. Fichero creado: {archivo_salida}") # Mostramos mensaje cuando finalice
    
    def exportar_json(self, archivo_salida):
        """Metodo para crear la salida en formato JSON y crear el arhcivo .json"""
        with open(archivo_salida, 'w', encoding='utf-8') as f:
            json.dump(self.resultados, f, ensure_ascii=False, indent=4)
        print(f"Resultados exportados a JSON. Fichero creado: {archivo_salida}") # Mostramos mensaje cuando finalice

    def mostrar_pantalla(self):
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("#", style="dim")
        table.add_column("Titulo", width=50)
        table.add_column("Descripción")
        table.add_column("Enlace")

        for indice, resultado in enumerate(self.resultados, start=1):
            table.add_row(str(indice), resultado["title"], resultado["description"], resultado["link"])
            table.add_row("", "", "", "")
            
        console.print(table)