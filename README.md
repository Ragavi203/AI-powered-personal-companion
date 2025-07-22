# AI Powered Personal Companion

Your personal AI that remembers everything - completely private, no cloud needed! Upload documents, record voice notes, and chat with your entire digital life using natural language.

## Use Cases

### Personal Knowledge Management
- Upload meeting notes, research papers, personal journals
- Ask: *"What did I decide about the marketing strategy last month?"*
- Get instant answers from your accumulated knowledge

### Voice Note Organization
- Record thoughts, ideas, meeting summaries on-the-go
- Automatic transcription with Whisper AI
- Ask: *"What ideas did I voice-record about the mobile app?"*

### Project Memory
- Track conversations, decisions, and progress across projects
- Ask: *"When did I last meet with Ragavi about the BCI project?"*
- Never lose context on long-running initiatives

### Personal Search Engine
- Natural language search across all your content
- Ask: *"Find everything related to Q2 planning"*
- Semantic search understands context, not just keywords

### Learning & Research
- Upload textbooks, articles, course materials
- Ask: *"Explain the key concepts from Chapter 5"*
- Build your personal tutor from your own materials

### Professional Assistant
- Store performance reviews, 1-on-1 notes, career goals
- Ask: *"What feedback did my manager give about presentation skills?"*
- Track your professional development journey

## Tech Stack

### Frontend & UI
- **Streamlit** - Clean, intuitive web interface
- **Python** - Core application logic

### AI & Machine Learning
- **Ollama** - Local LLM inference (Llama2/Mistral)
- **OpenAI Whisper** - Speech-to-text transcription
- **HuggingFace Transformers** - Text embeddings for semantic search

### Vector Database & Search
- **ChromaDB** - Vector storage for semantic search
- **LangChain** - RAG (Retrieval-Augmented Generation) pipeline
- **Sentence Transformers** - Text embedding models

### Document Processing
- **PyPDF2** - PDF text extraction
- **Python Standard Library** - Text file processing

### Development & Deployment
- **Python Virtual Environment** - Dependency isolation
- **Git** - Version control
- **Cross-platform** - Runs on Mac, Windows, Linux

## Quick Start

### Prerequisites
- Python 3.9+ installed
- Git installed

### 1. Install Ollama
```bash
# Download from ollama.ai or use package manager
brew install ollama  # macOS
# or download from https://ollama.ai

# Pull a model
ollama pull llama2
```

### 2. Clone & Setup
```bash
git clone https://github.com/Ragavi203/AI-powered-personal-companion.git
cd AI-powered-personal-companion

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the App
```bash
# Start Ollama (in separate terminal)
ollama serve

# Start the companion app
streamlit run app.py
```

Open your browser to `http://localhost:8501` and start building your personal AI companion!

## How to Use

### Upload Documents
1. **PDF Files**: Research papers, meeting notes, reports
2. **Text Files**: Journal entries, project notes, documentation

### Record Voice Notes
1. Upload audio files (MP3, WAV, M4A)
2. Automatic transcription via Whisper
3. Indexed for semantic search

### Ask Natural Questions
- *"What meetings did I have last week?"*
- *"Find notes about the BCI project"*
- *"When did I mention budget concerns?"*
- *"Summarize my thoughts on remote work"*

## Why This Matters

### Privacy First
- Everything runs locally on your machine
- No data sent to cloud services
- Your personal information stays personal

### Zero API Costs
- Uses free, open-source models
- No subscription fees or usage limits
- One-time setup, unlimited use

### True Personal AI
- Learns from YOUR content specifically
- Understands your personal context
- Grows smarter as you add more data

### Actually Useful
- Solves real productivity problems
- Natural language interface
- Instant search across all content

## Future Enhancements

- [ ] **Mobile App** - React Native companion
- [ ] **Calendar Integration** - Connect with Google Calendar/Outlook
- [ ] **Email Integration** - Index and search emails
- [ ] **Image OCR** - Extract text from images/screenshots
- [ ] **Web Clipper** - Save articles and web content
- [ ] **Export Features** - Generate reports and summaries
- [ ] **Multi-modal** - Image and video understanding
- [ ] **Collaboration** - Share knowledge bases (while keeping privacy)

## Contributing

This project represents the future of personal AI - completely private, actually useful, and accessible to everyone. Contributions welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- **Ollama** for making local LLMs accessible
- **OpenAI** for Whisper speech recognition
- **ChromaDB** for vector database technology
- **Streamlit** for rapid UI development
- **HuggingFace** for embedding models

---

**Built with care for the future of personal AI**

*"Your AI companion that actually remembers your life - because your thoughts and ideas deserve better than being lost in the digital void."*
