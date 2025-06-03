# Stock  Analyst

An Agentic, multi-agent system that combines real-time stock analysis, financial metrics, and web search using **Phidata**, **Groq LLaMA3**, and **yFinance**. Built for investors and analysts to research about financial analysis of any stock in the market.

> This is powered by Groq’s LLaMA3 · Built with Phidata · Streamlined with FastAPI ·
---

## Features

- **Web Search Agent** – Retrieves live financial news using DuckDuckGo.
- **Finance Agent** – Provides stock fundamentals, analyst ratings, ratios, and trends.
- **Multi-Agent Collaboration** – Agents work in tandem to deliver structured insights.
- **Playground Mode** – Visual interface powered by Phidata's playground on `localhost:7777`.

---
## General Info

| Tool              | Purpose                                |
| ----------------- | -------------------------------------- |
| **Phidata**       | Agent framework for building, deploying, and monitoring AI agents  |
| **Groq (LLaMA3)** | Transformer-based LLM            |
| **YFinance**      | Stock data: prices, ratios, indicators |
| **DuckDuckGo**    | Fetches latest news and articles       |
| **FastAPI**       | Playground deployment support          |
| **dotenv**        | Secure key management                  |

---

## File Structure
```
Stock_Analyst/
├── financial_agent.py # AI agents
├── phidata_playground.py # Launches Phidata UI (http://localhost:7777)
├── .env # API keys
├── requirements.txt # Dependencies
├── LICENSE # Project license
└── README.md # You are here!
```
---

## Setup Instructions

### Clone the Repository

```
git clone https://github.com/itsabhishekm/Stock_Analyst.git
cd Stock_Analyst
```

### Create a Virtual Environment & Install Dependencies

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

```
### Seting Up Environment Variables

Create a .env file in the root directory and past your API KEYS:

```
PHI_API_KEY="your-phidata-api-key"
GROQ_API_KEY="your-groq-api-key"
OPENAI_API_KEY="your-openai-api-key"
```

### Run Agents in CLI Mode

```
python financial_agent.py
```
This will trigger both the web search and financial agents to respond to a sample query like:
"Summarize analyst recommendations and share the latest news for NVDA"

### Launch Phidata Playground (Web UI)

```
python phidata_playground.py
```
Then login to your Phidata account, and select localhost:7777 from the endpoint list.
