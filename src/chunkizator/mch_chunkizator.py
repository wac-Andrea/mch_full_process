import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter

class ChunkSplitter:
    def __init__(self):
        pass

    def create_chunks(self, text, chunk_size=750, chunk_overlap=100, model="gpt-4"):
        TextSplitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=lambda text: self.count_tokens(text, model),
            separators=["\f", "\n", ". "],
        )
        documents = TextSplitter.create_documents([text])
        return [d.page_content for d in documents]
    
    
    @staticmethod
    def count_tokens(text, model="gpt-4-"):
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    
if __name__ == "__main__":
    pass
