from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

META_PROMPT = """
Tengo una frase mal escrita con símbolos extraños, palabras mal ordenadas, palabras mal separadas o con faltas de ortografía. 
Necesito que me devuelvas la frase correctamente escrita, con buena puntuación y con las palabras corregidas. 
Sólo corrige la frase, no añadas información o palabras que no vengan en el prompt del usuario. 
Además, traduce al español los caracteres especiales o códigos. 
Haz tu mejor esfuerzo para interpretar el significado y traducirlo de manera precisa.
Por añadir contexto, todas las frases que vas a analizar una a una están extraídas de manuales de carretillas 
eléctricas y otras herramientas de trabajo
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

