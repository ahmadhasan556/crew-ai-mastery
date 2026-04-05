# 🚀 CrewAI Learning & Projects

This repository contains a collection of **CrewAI experiments and
projects** built while learning multi-agent AI systems using **CrewAI,
Ollama, and custom tools**.

The goal of this repo is to understand how **AI agents collaborate to
complete complex tasks** such as research, marketing strategy, and
content creation.

---

# 📂 Project Structure

    CREW-AI
    │
    ├── 1.email_agent
    │   └── 1.email_agent.ipynb
    │
    ├── 2.email_agent_with_custom_tool
    │   └── 2.email_agent_with_c_tool.ipynb
    │
    ├── 3.crew_research
    │   └── 3.crew_research.ipynb
    │
    ├── 4.crew_research_with_web_tools
    │   └── 4.crew_research_with_web_tools.ipynb
    │
    ├── 5.research_yaml
    │   ├── config/
    │   └── 5.yaml.py
    │
    ├── 6.marketing-crew
    │   ├── config/
    │   ├── blog_keywords_competitors.md
    │   ├── content_calendar
    │   └── crew.py

---

# 🧠 What This Repository Contains

## 1️⃣ Email Agent

A simple AI agent that generates emails automatically.

Features: - Email generation - Prompt based responses - Basic CrewAI
agent usage

---

## 2️⃣ Email Agent with Custom Tool

An improved email agent with a **custom tool integration**.

Features: - Custom tool usage - Agent tool calling - Structured outputs

---

## 3️⃣ Crew Research

A **multi-agent research system**.

Agents: - Research agent - Writer agent

Features: - Multi-agent collaboration - Task delegation - Structured
research output

---

## 4️⃣ Crew Research with Web Tools

Adds **web search and scraping tools** to research agents.

Tools used: - Search tool - Web scraping - Content extraction

---

## 5️⃣ Research using YAML Configuration

Example of defining **agents and tasks using YAML configuration**.

Features: - YAML based agent configuration - YAML based task
definition - Cleaner project architecture

---

## 6️⃣ Marketing Crew (Advanced Project)

A **multi-agent AI marketing team**.

Agents: - Head of Marketing - Social Media Content Creator - Blog
Writer - SEO Specialist

Capabilities: - Market research - Marketing strategy - Social media
content - Blog writing - SEO optimization

This project simulates a **complete AI marketing department**.

---

# ⚙️ Technologies Used

- CrewAI
- Ollama (Local LLMs)
- Python
- Pydantic
- SerpAPI
- Web scraping tools

---

# 🤖 Local LLM

Example model used:

    qwen2.5:7b

Run Ollama server:

    ollama serve

Pull model:

    ollama pull qwen2.5:7b

---

# 🛠 Installation

Clone the repository:

    git clone https://github.com/yourusername/crew-ai-projects.git

Install dependencies:

    pip install crewai crewai-tools python-dotenv serpapi

---

# 🔑 Environment Variables

Create `.env` file:

    SERPAPI_API_KEY=your_api_key

---

# ▶️ Running the Project

Example: run marketing crew

    python crew.py

Agents will collaborate to produce: - marketing strategy - blogs -
social posts - SEO optimized content

---

# 📚 Learning Goals

This repository demonstrates:

- Multi-agent systems
- Agent collaboration
- Tool usage in AI agents
- Local LLM integration
- Automated workflows

---

# 👨‍💻 Author

**Ahmad Hassan**\
Software Engineer \| Mobile App Developer \| AI Agents
