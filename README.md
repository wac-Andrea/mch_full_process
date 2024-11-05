# Comando de ejecución: 
python main.py <nombreArchivo.pdf>

# Instalar: 
pip install pdfplumber
pip install openai
pip install python-dotenv
pip install tiktoken
pip install langchain
pip install pinecone (y actualizarlo con python.exe -m pip install --upgrade pip)
pip install pinecone

# Resumen:
Pequeño programa que extrae el texto de un archivo PDF y lo divide en chunks más pequeños para ser revisados y corregidos mediante un prompt por OpenAI. Finalmente, este texto es pasado a vectores que se indexan en una base de datos vectorial (Pinecone). 
