archivo_salida = args.txt_salida
text_from_pdf = leer_pdf()

chuncks = chunckizator(archivo_salida)

corrected_texts = texts_to_api(chuncks)
generate_embeddings(corrected_texts)