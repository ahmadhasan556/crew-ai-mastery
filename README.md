# 🚀 CrewAI Learning Lab

A teaching-focused repository for learning **Multi-Agent AI systems
using CrewAI**.

This repository contains **step-by-step learning projects** built while
exploring how AI agents collaborate to complete complex tasks such as:

- Research automation
- Email generation
- Marketing strategy
- Blog writing
- Web data extraction

The goal of this repository is to help developers **learn CrewAI through
practical examples and experiments**.

---

# 📂 Learning Project Structure

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

# 🧠 Learning Modules

## 1️⃣ Email Agent

A beginner example showing how to create a **basic CrewAI agent** that
generates emails.

Key Concepts: - Agent creation - Prompt-based responses - Basic CrewAI
workflow

---

## 2️⃣ Email Agent with Custom Tool

Extends the basic email agent by integrating a **custom tool**.

Key Concepts: - Tool creation - Tool calling by agents - Structured
outputs

---

## 3️⃣ Crew Research (Multi-Agent System)

A simple **two-agent system** that performs research and writing.

Agents: - Research Agent - Writer Agent

Key Concepts: - Multi-agent collaboration - Task delegation - Structured
outputs

---

## 4️⃣ Crew Research with Web Tools

Adds **internet capabilities** to agents.

Tools Used: - Search tools - Web scraping - Content extraction

Key Concepts: - External tools - Real-time research - Data extraction

---

## 5️⃣ YAML Configuration for Agents

Demonstrates how to configure **agents and tasks using YAML files**.

Key Concepts: - YAML agent configuration - YAML task definitions - Clean
project architecture

---

## 6️⃣ Marketing Crew (Advanced Project)

A complete **AI Marketing Team simulation**.

Agents: - Head of Marketing - Social Media Content Creator - Blog
Writer - SEO Specialist

Capabilities: - Market research - Marketing strategy creation - Blog
writing - Social media content - SEO optimization

This example simulates a **fully automated AI marketing department**.

---

# ⚙️ Technologies Used

- CrewAI
- Python
- Ollama (Local LLMs)
- Pydantic
- SerpAPI
- Web Scraping Tools

---

# 🤖 Local LLM Setup

Example model used:

    qwen2.5:7b

Start Ollama:

    ollama serve

Pull the model:

    ollama pull qwen2.5:7b

---

# 🛠 Installation

Clone the repository:

    git clone https://github.com/yourusername/crew-ai-projects.git

Install dependencies:

    pip install crewai crewai-tools python-dotenv serpapi

---

# 🔑 Environment Variables

Create a `.env` file:

    SERPAPI_API_KEY=your_api_key

---

# ▶️ Running the Project

Example: run the marketing crew

    python crew.py

The agents will collaborate to generate:

- Marketing strategy
- Blog content
- Social media posts
- SEO optimized articles

---

# 📚 Learning Objectives

This repository demonstrates:

- Multi-agent AI systems
- Agent collaboration
- Tool integration with agents
- Local LLM usage
- Automated AI workflows

---

# 👨‍💻 Author

**Ahmad Hassan**\
Software Engineer \| Mobile App Developer \| AI Agents
