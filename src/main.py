import argparse
from leer_pdf.mch_leer_pdf import extract_text_from_pdf
from chunkizator.mch_chunkizator import ChunkSplitter
from normalizador.mch_normalizador import generate_prompt, texts_to_api

def main():
    parser = argparse.ArgumentParser(description="Extract text from a PDF file.")
    parser.add_argument("pdf_path", type=str, help="Path to the input PDF file.")
    args = parser.parse_args()

    extracted_txt=extract_text_from_pdf(args.pdf_path)
   
    splitter = ChunkSplitter()
    chunks = splitter.create_chunks(extracted_txt, chunk_size=50, chunk_overlap=5, model="gpt-4")
    for i, chunk in enumerate(chunks):
        print(f"Fragmento {i+1}: {chunk}")

    corrected_texts = []
    for chunk in chunks:
        corrected_text = generate_prompt(chunk)  
        corrected_texts.append(corrected_text)

    for corrected in corrected_texts:
        print(f"Texto Corregido: {corrected}\n")

    """  text_list = [chunks]
    corrected_texts = texts_to_api (text_list)
    for corrected in corrected_texts:
        print(f"Textos corregidos: {corrected}\n")
    """

#archivo_salida = args.txt_salida
#text_from_pdf = leer_pdf()

#chunks = chunckizator(archivo_salida)
# splitter = ChunkSplitter()
# chunks = splitter.create_chunks(salida.txt, chunk_size=50, chunk_overlap=5, model="gpt-4")


#corrected_texts = texts_to_api(chunks)
#generate_embeddings(corrected_texts)

if __name__ == "__main__":
    main()