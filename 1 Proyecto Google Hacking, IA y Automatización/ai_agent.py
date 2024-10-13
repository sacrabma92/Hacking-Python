from gpt4all import GPT4All

class IAAgent:

    def __init__(self, model="Meta-Llama-3-8B-Instruct.Q4_0.gguf"):
        self.model = GPT4All(model)

    def generate_gdork(self, description):
        # Construimos el prompt
        prompt = self._build_prompt(description)
        try:
            output = self.model.generate(prompt)
            return output
        except Exception as e:
            print(f"Error al generar Google Dork: {e}")
            return None
            

    def _build_prompt(self, description):
        # Construimos el prompt
        return f"""Genera un Google Dork específico basado en la descripción del usuario. Un Google Dork utiliza operadores avanzados en motores de búsqueda para encontrar información específica que es difícil de encontrar mediante una búsqueda normal. Tu tarea es convertir la descripción del usuario en un Google Dork preciso. A continuación, se presentan algunos ejemplos de cómo deberías formular los Google Dorks basándote en diferentes descripciones:

        Descripción: Documentos PDF relacionados con la seguridad informática publicados en el último año.
        Google Dork: filetype:pdf "seguridad informática" after:2023-01-01

        Descripción: Presentaciones de Powerpoint sobre cambio climático disponibles en sitios .edu.
        Google Dork: site:.edu filetype:ppt "cambio climático"

        Descripción: Listas de correos electrónicos en archivos de texto dentro de dominios gubernamentales.
        Google Dork: site:.gov filetype:txt "email" | "correo electrónico"

        Ahora, basado en la siguiente descripción proporcionada por el usuario, genera el Google Dork correspondiente:

        Descripción: {description}"""
            
if __name__ == "__main__":
    description = "Listado de usuarios y contraseñas en el contenido de ficheros de texto"
    iaagent = IAAgent()
    print(iaagent.generate_gdork(description))