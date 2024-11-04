import tiktoken
"""Tiktoken provides methods to encode text in a way that counts tokens
(units of text) for language models."""

from langchain.text_splitter import RecursiveCharacterTextSplitter
"""It can split long pieces of text into smaller chunks."""

import argparse

class ChunkSplitter:
    def __init__(self):
        pass
    """Defines an initializer method (__init__) that doesn’t do anything in this case 
    (pass means no action)."""

    def create_chunks(self, text, chunk_size=750, chunk_overlap=100, model="gpt-4"):

        """Text (text to be split); chunck_size (maximum length of each text chunk); 
        chunck_overlap (number of characters each chunk should overlap with the previous chunk)"""
       
        TextSplitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=lambda text: self.count_tokens(text, model),
            separators=["\f", "\n", ". "],
        )

        """TextSplitter = Creates an instance of RecursiveCharacterTextSplitter called TextSplitter, with the following options:
                chunk_size: Maximum number of characters in each chunk (default is 750).
                chunk_overlap: Number of characters of overlap between each chunk (default is 100).
                length_function: Points to self.count_tokens, which will measure the length of each chunk in tokens.
                separators: Defines characters (\f, \n, and . ) to split by, prioritizing these as boundaries to start a new chunk."""
        
        documents = TextSplitter.create_documents([text])

        """Splits the text into smaller parts using TextSplitter.create_documents, which returns a list of document chunks."""
        
        return [d.page_content for d in documents]
    
    """Returns a list of chunk texts by taking the page_content (actual text) from each Document object in documents."""

    """Defines a static method (a function that doesn’t depend on class instances) called count_tokens, 
    which counts tokens in a given text for a language model."""
    
    @staticmethod
    def count_tokens(text, model="gpt-4-"):
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    
    """Encodes text into tokens and returns the number of tokens (length of the encoded list)."""

# Ejemplo de uso:
if __name__ == "__main__":
    pass

"""Para usar este código: 
    1.  Bash: pip install tiktoken langchain
    2.  Launch: python chunkizator.py"""
