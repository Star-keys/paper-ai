# Paper AI Agent

AI agent system for analyzing research papers in PDF format

## Features

### 1. Paper Analysis Agent (PaperAnalysisAgent)
- Provides concise summaries of key paper content
- Summarizes research topic, methodology, and main results within 10 lines
- **Endpoint**: `POST /papers/{paper_id}/analyze`

### 2. Scientist Agent (ScientistAgent)
Analyzes papers from a researcher's perspective aiming to formulate new hypotheses
- **Research Core Summary**: Organizes the paper's topic, methodology, and findings
- **Research Gap Analysis**: Identifies limitations and areas requiring further research
- **New Hypothesis Proposal**: Suggests 2-3 research hypotheses based on the paper
- **Follow-up Research Ideas**: Proposes experimental designs and research methods to validate hypotheses
- **Endpoint**: `POST /papers/{paper_id}/scientist`

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| POST | `/papers/{paper_id}/analyze` | Paper summary analysis |
| POST | `/papers/{paper_id}/scientist` | Scientist perspective analysis |

## How to Run

```bash
python main.py
```

After starting the server, visit http://localhost:8000

## Contact

Email us: zoloman316@gmail.com
