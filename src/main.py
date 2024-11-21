import argparse
import os
from dotenv import load_dotenv
from leer_pdf.mch_leer_pdf import extract_text_from_pdf
from chunkizator.mch_chunkizator import ChunkSplitter
from normalizador.mch_normalizador import generate_prompt
from crear_embedding.crear_embedding import CrearEmbeddings
from almacenar_embedding.almacenar_embedding import AlmacenarEmbedding
from comprobar_encoding.comprobar_encoding import classify_full_text

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF file.")
    parser.add_argument("pdf_path", type=str, help="Path to the input PDF file.")
    args = parser.parse_args()

    extracted_txt = extract_text_from_pdf(args.pdf_path)
    
    language = classify_full_text(extracted_txt)
    print(f"Classified language of full text as: {language}")
    
    splitter = ChunkSplitter()
    chunks = splitter.create_chunks(extracted_txt, chunk_size=750, chunk_overlap=100, model="gpt-4")

    if language == 'english':
        english_chunks = chunks  
        for chunk in english_chunks:
            corrected_text = generate_prompt(chunk)
            corrected_texts.append(corrected_text)
            print(f"Corrected non-Latin text: {corrected_text}")
            print("English chunk:", chunk)
    
    elif language == 'spanish':
        spanish_chunks = chunks  
        for chunk in spanish_chunks:
            print("Spanish chunk:", chunk)
    
    else:
        non_latin_chunks = chunks  
        corrected_texts = []
        for chunk in non_latin_chunks:
            corrected_text = generate_prompt(chunk)
            corrected_texts.append(corrected_text)
            print(f"Corrected non-Latin text: {corrected_text}")

    
    all_texts = (english_chunks if language == 'english' else []) + \
                (spanish_chunks if language == 'spanish' else []) + \
                (corrected_texts if language == 'non_latin' else [])


    
    embeddings = CrearEmbeddings(all_texts, model="text-embedding-3-small")
    print(embeddings)

    
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    storage_responses = AlmacenarEmbedding(embeddings, api_key=pinecone_api_key, index="mch-carretillas-chatbot")
    
   
    for i, response in enumerate(storage_responses):
        print(f"Stored vector {i+1}: {response}") 

if __name__ == "__main__":
    main()
