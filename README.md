# CrewAI Practice Projects

This repository is a small collection of CrewAI experiments and examples. It starts with simple notebook-based agents and builds up to YAML-configured crews and a larger multi-agent marketing workflow.

## What is in this repo

- `1.email_agent/`
  Single-agent notebook that rewrites a rough email into a clearer, more professional version.
- `2.email_agent_with_custom_tool/`
  Similar email example, but adds a custom CrewAI tool to simplify jargon before producing the final draft.
- `3.crew_research/`
  Two-agent research and writing notebook.
- `4.crew_research_with_web+tools/`
  Research crew notebook that adds web search through `SerperDevTool`.
- `5.research_yaml/`
  A YAML-driven research and writing crew defined in Python and configured through `config/agent.yaml` and `config/tasks.yaml`.
- `6.marketing-crew/`
  A larger marketing workflow with agents for market research, strategy, social content, blog writing, and SEO.

## Tech Stack

- Python
- CrewAI
- `crewai-tools`
- Jupyter notebooks
- `python-dotenv`
- `serpapi`
- Ollama with `qwen2.5:7b` for the script-based examples
- Gemini 2.5 Flash in the notebook-based examples

## Setup

Because this repo does not currently include a dependency manifest, install the packages manually in a virtual environment.

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install crewai crewai-tools python-dotenv serpapi jupyter ipykernel pydantic
```

If you want to run the Python scripts in folders `5.research_yaml` and `6.marketing-crew`, make sure Ollama is running locally and the model used by the code is available:

```powershell
ollama pull qwen2.5:7b
ollama serve
```

The script-based examples expect Ollama at `http://localhost:11434`.

## Environment Variables

Create a `.env` file in the project root and add the keys your examples need.

```env
GEMINI_API_KEY=your_key_here
SERPER_API_KEY=your_key_here
```

Notes:

- The notebooks use Gemini-based CrewAI LLM configuration.
- The Python scripts use `serpapi.GoogleSearch`, but the current code reads the key from `SERPER_API_KEY`. Keep that variable name unless you plan to refactor the scripts.
- `.env` should stay local and should not be committed.

## How To Run

### Notebook examples

Start Jupyter from the repository root:

```powershell
jupyter notebook
```

Then open any of these notebooks:

- `1.email_agent/1.email_agent.ipynb`
- `2.email_agent_with_custom_tool/2.email_agent_with_c_tool.ipynb`
- `3.crew_research/3.crew_research.ipynb`
- `4.crew_research_with_web+tools/4.crew_research_with_web_tools.ipynb`

### YAML research crew

Run this from inside `5.research_yaml` so the relative config paths resolve correctly:

```powershell
cd 5.research_yaml
python .\5.yaml.py
```

### Marketing crew

Run this from inside `6.marketing-crew` so the config files load correctly:

```powershell
cd 6.marketing-crew
python .\crew.py
```

## Project Notes

- `5.research_yaml` and `6.marketing-crew` rely on relative config paths, so run them from their own folders.
- The marketing workflow is configured to generate strategy, content calendar, drafts, reel scripts, blogs, and SEO outputs.
- Some task descriptions reference output folders such as `resources/drafts/...`. Create those folders if you want file outputs to be written there during local runs.

## Suggested Next Improvements

- Add a root `requirements.txt` or `pyproject.toml`.
- Add a `.env.example` file with placeholder variables only.
- Add output folders used by the marketing crew.
- Clean up naming inconsistencies such as `SERPER_API_KEY` being used for a SerpApi-based search tool.
