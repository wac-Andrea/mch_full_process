from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

META_PROMPT = """
Tengo un texto compuesto por diferentes frases que están mal escritas con símbolos extraños, palabras mal ordenadas, palabras mal separadas o con faltas de ortografía. 
Necesito que me devuelvas estas frases correctamente escritas, con buena puntuación y con las palabras corregidas. 
Sólo corrige el texto, no añadas información o palabras que no vengan en el prompt del usuario. 
Si encuentras oraciones o palabras en otro idioma, tradúcelas correctamente al español.
Hazlo sólo con aquellas oraciones que contengan verbo; las palabras que no formen parte de una oración con verbo déjalas fuera de tu respuesta.
Mantén el formato de párrafo de las oraciones que me des en tu respuesta.  
Si el texto no contiene oraciones con verbo, devuelve una respuesta en blanco sin ningún mensaje.
""".strip()

def generate_prompt(task_or_prompt: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": META_PROMPT,
            },
            {
                "role": "user",
                "content": task_or_prompt,
            },
        ],
    )
    return completion.choices[0].message.content

def texts_to_api(text_list: list) -> list:
    corrected_texts = []
    for text in text_list:
        corrected_text = generate_prompt(text)
        corrected_texts.append(corrected_text)
    return corrected_texts

