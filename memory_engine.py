import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
from datetime import datetime

class MemoryEngine:
    def __init__(self, persist_directory="./vector_store"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection("memory")
        self.embeddings = HuggingFaceEmbeddings()
        
    def add_document(self, text, metadata=None):
        """Add text to memory with metadata"""
        if metadata is None:
            metadata = {"timestamp": datetime.now().isoformat()}
            
        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        chunks = text_splitter.split_text(text)
        
        # Add to vector store
        for i, chunk in enumerate(chunks):
            doc_id = f"{metadata.get('filename', 'doc')}_{i}_{datetime.now().timestamp()}"
            self.collection.add(
                documents=[chunk],
                metadatas=[metadata],
                ids=[doc_id]
            )
    
    def search_memory(self, query, n_results=5):
        """Search through memory"""
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results