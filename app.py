import streamlit as st
from memory_engine import MemoryEngine
from audio_processor import AudioProcessor
import PyPDF2
import requests
import json
from datetime import datetime
import os

# Initialize
if 'memory_engine' not in st.session_state:
    st.session_state.memory_engine = MemoryEngine()
if 'audio_processor' not in st.session_state:
    st.session_state.audio_processor = AudioProcessor()

st.set_page_config(page_title="Personal Memory GPT 🧠", layout="wide")

def query_ollama(prompt, context=""):
    """Query local Ollama LLM"""
    full_prompt = f"""Context from your memory:
{context}

Question: {prompt}

Based on the context above, provide a helpful answer. If the context doesn't contain relevant information, say so."""
    
    try:
        response = requests.post('http://localhost:11434/api/generate',
            json={
                'model': 'llama2',  # or 'mistral'
                'prompt': full_prompt,
                'stream': False
            })
        
        if response.status_code == 200:
            return response.json()['response']
        else:
            return "Error: Could not connect to Ollama. Make sure it's running."
    except:
        return "Error: Ollama not available. Please install and run Ollama."

def extract_pdf_text(pdf_file):
    """Extract text from PDF"""
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# UI
st.title("🧠 Personal Memory GPT")
st.subheader("Chat with your life - upload docs, voice notes, and ask questions!")

# Sidebar for uploads
with st.sidebar:
    st.header("📁 Add to Memory")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Upload Document", 
        type=['txt', 'pdf'],
        help="Upload text files or PDFs"
    )
    
    if uploaded_file and st.button("💾 Add Document"):
        filename = uploaded_file.name
        
        if filename.endswith('.pdf'):
            text = extract_pdf_text(uploaded_file)
        else:
            text = str(uploaded_file.read(), "utf-8")
        
        # Add to memory
        metadata = {
            "filename": filename,
            "type": "document",
            "timestamp": datetime.now().isoformat()
        }
        
        st.session_state.memory_engine.add_document(text, metadata)
        st.success(f"✅ Added {filename} to memory!")
    
    st.divider()
    
    # Audio upload
    audio_file = st.file_uploader(
        "Upload Voice Note",
        type=['mp3', 'wav', 'm4a'],
        help="Upload audio files to transcribe"
    )
    
    if audio_file and st.button("🎤 Transcribe & Add"):
        with st.spinner("Transcribing audio..."):
            text = st.session_state.audio_processor.transcribe_audio(audio_file)
            
            metadata = {
                "filename": audio_file.name,
                "type": "voice_note", 
                "timestamp": datetime.now().isoformat()
            }
            
            st.session_state.memory_engine.add_document(text, metadata)
            st.success("✅ Voice note transcribed and added!")
            st.write("**Transcription:**", text[:200] + "...")

# Main chat interface
st.header("💬 Chat with Your Memory")

# Chat input
user_query = st.text_input(
    "Ask me anything about your uploaded content:",
    placeholder="When did I last meet with Ragavi about the BCI project?"
)

if user_query:
    with st.spinner("Searching memory..."):
        # Search memory
        search_results = st.session_state.memory_engine.search_memory(user_query)
        
        # Prepare context
        context = ""
        if search_results['documents'][0]:
            for doc, metadata in zip(search_results['documents'][0], search_results['metadatas'][0]):
                context += f"[{metadata.get('filename', 'Unknown')}]: {doc}\n\n"
        
        # Query LLM
        response = query_ollama(user_query, context)
        
        # Display response
        st.write("**🤖 Response:**")
        st.write(response)
        
        # Show sources
        if search_results['documents'][0]:
            with st.expander("📚 Sources"):
                for i, (doc, metadata) in enumerate(zip(search_results['documents'][0], search_results['metadatas'][0])):
                    st.write(f"**Source {i+1}:** {metadata.get('filename', 'Unknown')}")
                    st.write(doc[:300] + "...")
                    st.divider()

# Quick examples
st.header("💡 Example Queries")
examples = [
    "What meetings did I have last week?",
    "Find notes about the BCI project", 
    "When did I mention Ragavi?",
    "What were my goals for May 2024?",
    "Summarize my voice notes from yesterday"
]

cols = st.columns(len(examples))
for col, example in zip(cols, examples):
    if col.button(example, key=example):
        st.rerun()