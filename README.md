# Smart Search Researcher

A local AI Agent that connects an LLM to the live internet using LangGraph.

This project implements a "Research Agent" that autonomously searches the web for a given topic and summarizes the findings. It demonstrates the use of **Agentic AI** patterns by cycling between a search tool and a reasoning model.

## ⚡️ Tech Stack

* **Orchestration:** [LangGraph](https://langchain-ai.github.io/langgraph/) (StateGraph)
* **Inference Engine:** [Groq](https://groq.com/) (Llama 3 70B)
* **Tools:** [Tavily API](https://tavily.com/) (Search optimized for RAG/Agents)
* **Interface:** Streamlit

## 🛠️ Architecture

The agent operates on a graph-based workflow:
1.  **Input:** Accepts a research topic.
2.  **Search Node:** Uses Tavily to fetch real-time data from the web.
3.  **Summarize Node:** Uses Llama 3 (via Groq) to synthesize the raw search data into a clean insight.
4.  **Output:** Returns a concise, referenced summary.

## 🚀 Setup & Run

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd smart-search-agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up API Keys:**
    Create a `.env` file in the root directory:
    python3 -m venv venv
    source venv/bin/activate
    ```env
    GROQ_API_KEY=gsk_...
    TAVILY_API_KEY=tvly_...
    ```

4.  **Run the Agent:**
    ```bash
    streamlit run app.py
    ```