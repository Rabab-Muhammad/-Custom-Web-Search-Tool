## 🌐 Custom Web Search Tool – Assignment 7

It is a Python-based AI Agent that integrates with Google Gemini API and Tavily Web Search API to answer user queries in real-time.

## 🚀 Features
 - 🤖 LLM-powered Agent using Google Gemini (via OpenAI-style SDK)
 - 🔍 Custom Web Search Tool (Tavily API) for real-time knowledge
 - 🖥️ Command-Line Interface (CLI) for interactive queries
 - 🛠️ Built using OpenAI Agents SDK
 - ⚡ Async architecture for smooth performance

## 📂 Project Structure
```bash
Custom-Web-Search-Tool-assignment-7/
│── main.py          # Entry point: runs the interactive CLI
│── tools.py         # Tavily web search tool function
│── tavily_api.py    # Handles API calls to Tavily
│── agents.py        # Agent + Runner setup
│── .env             # Environment variables (API keys)
```
## Setup Environment Variables
Create a .env file in the root folder:

```ini
GEMINI_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## ▶️ Usage
Run the agent with:
```bash
python main.py
```
You’ll see:
```vbnet
🌐 Welcome to Custom Web Search Agent! (type 'exit' to quit)

🔎 Ask me anything: Who is the current Prime Minister of Pakistan?
🤖 Agent: The current Prime Minister of Pakistan is ...
```

