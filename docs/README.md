# Project Documentation

## Architecture
This project implements a Retrieval-Augmented Generation (RAG) system
to navigate and explain large code repositories.

### Workflow
1. Ingest GitHub repositories
2. Parse files and chunk code
3. Generate embeddings
4. Store vectors in FAISS
5. Retrieve relevant context
6. Generate answers using LLM

## Components
- Code parser
- Embedding generator
- Vector database
- Retrieval engine
- LLM-based explanation module

## Future Enhancements
- VS Code extension
- Multi-repository support
- Agent-based reasoning
