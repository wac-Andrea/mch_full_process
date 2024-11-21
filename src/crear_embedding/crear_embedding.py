from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def CrearEmbeddings(listas_datos, model="text-embedding-3-small", unique_id=None):
    lista_vectores = []
    for item in listas_datos:
        item = ' '.join(item.split())  
        item.replace("\n", " ")  
        try:
            response = client.embeddings.create(input=str(item), model=model)
            embedding = {
                "value": response.data[0].embedding,    
                "metadata": item,
               
            }

            if unique_id:
                embedding["id"] = unique_id
                
            lista_vectores.append(embedding)
            
        except Exception as e:
            print("[EMBEDDINGS] An error occurred during the creation of embeddings:", str(e))
    return lista_vectores