import whisper
import streamlit as st
import tempfile
import os

class AudioProcessor:
    def __init__(self):
        
        self.model = None
    
    def load_model(self):
        """Load Whisper model (cached)"""
        if self.model is None:
            self.model = whisper.load_model("base")
        return self.model
    
    def transcribe_audio(self, audio_file):
        """Transcribe audio file to text"""
        model = self.load_model()
        
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(audio_file.read())
            tmp_path = tmp_file.name
        
        try:
            result = model.transcribe(tmp_path)
            return result["text"]
        finally:
            os.unlink(tmp_path)