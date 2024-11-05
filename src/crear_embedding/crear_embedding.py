from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # Carga todas las variables del .env como variables de entorno

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Busca entre las variables de entorno una que se llame "OPENAI_API_KEY"

def CrearEmbeddings(listas_datos, model="text-embedding-3-small", unique_id=None):
    lista_vectores = []
    #Initializes an empty list called lista_vectores, which will store the embedding data for each item in listas_datos.

    for item in listas_datos:
    #Begins a loop that iterates through each element (item) in listas_datos. Each item represents a piece of text that will be embedded.
        item = ' '.join(item.split())  # Elimina espacios en blanco de más
        item.replace("\n", " ")  # Reemplaza saltos de línea por un espacio
        try:
            response = client.embeddings.create(input=str(item), model=model)
            #input=str(item): Converts item to a string format to ensure compatibility.
            embedding = {
                "value": response.data[0].embedding,
                #Extracts the embedding vector from the API response, which is expected to be stored in response.data[0].embedding.
                "metadata": item,
                #Stores the original (cleaned) text item as metadata in the dictionary.
            }

            # Add 'id' only if unique_id is provided
            if unique_id:
                embedding["id"] = unique_id
                #If unique_id is not None, adds an "id" key to the embedding dictionary with unique_id as its value.

            lista_vectores.append(embedding)
            #Appends the embedding dictionary to the lista_vectores list.

        except Exception as e:
            print("[EMBEDDINGS] An error occurred during the creation of embeddings:", str(e))
    return lista_vectores