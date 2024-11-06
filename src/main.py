import argparse
import os
from dotenv import load_dotenv
from leer_pdf.mch_leer_pdf import extract_text_from_pdf
from chunkizator.mch_chunkizator import ChunkSplitter
from normalizador.mch_normalizador import generate_prompt
from crear_embedding.crear_embedding import CrearEmbeddings
from almacenar_embedding.almacenar_embedding import AlmacenarEmbedding
from comprobar_encoding.comprobar_enconding import is_latin

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF file.")
    parser.add_argument("pdf_path", type=str, help="Path to the input PDF file.")
    args = parser.parse_args()

    extracted_txt=extract_text_from_pdf(args.pdf_path)

    if is_latin(extracted_txt):
        print("The extracted text is likely in English or Spanish.")
    else:
        print("The extracted text contains unsupported characters (likely Chinese or symbols).")
        
   
      
    splitter = ChunkSplitter()
    chunks = splitter.create_chunks(extracted_txt, chunk_size=750, chunk_overlap=100, model="gpt-4")
    for i, chunk in enumerate(chunks):
        print(f"Fragmento {i+1}: {chunk}")

    corrected_texts = []
    for chunk in chunks:
        corrected_text = generate_prompt(chunk)  
        corrected_texts.append(corrected_text)

    for corrected in corrected_texts:
        print(f"Texto Corregido: {corrected}\n")
        print(type(corrected_texts))

    embeddings = CrearEmbeddings(corrected_texts, model="text-embedding-3-small")

    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    storage_responses = AlmacenarEmbedding(embeddings, api_key=pinecone_api_key, index="mch-dev")
    
    for i, response in enumerate(storage_responses):
        print(f"Vector almacenado: {i+1}: {response}")
 
if __name__ == "__main__":
    main()