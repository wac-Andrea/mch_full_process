import uuid
from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()  

def AlmacenarEmbedding(lista_vectores, api_key, index="mch-dev", namespace="ns1"):
    pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
    indexPC = pc.Index(index)
    
    responses = []
    for vector in lista_vectores:
        vector_estructurado = (
            {
                "id": vector.get("id", str(uuid.uuid4())),
                "values": vector["value"],
                "metadata": {"resumen": vector["metadata"]},
            },
        )
        try:
            response = indexPC.upsert(vectors=vector_estructurado, namespace=namespace)
            responses.append(response)
        except Exception as e:
            # Return the error and stop the function
            return f"An error occurred: {str(e)}"
    return responses
 