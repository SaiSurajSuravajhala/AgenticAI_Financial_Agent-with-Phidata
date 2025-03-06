# Agentic AI Search Interface

This project is a multi-agent system built using the **phi.agent** framework. It integrates with **OpenAIChat**, **YFinanceTools**, and **DuckDuckGo** to provide real-time financial insights and web search results. The application is delivered through a Streamlit UI that displays formatted output and even includes a custom background image.

## Project Overview

- **Multi-Agent Setup:**  
  Two specialized agents are combined:
  - **Web Search Agent:** Retrieves web-based information and sources using DuckDuckGo.
  - **Finance AI Agent:** Fetches financial data such as stock prices, analyst recommendations, fundamentals, and company news via YFinance tools.

- **User Interface:**  
  The Streamlit-based UI allows users to enter a query (e.g., "Summarize analyst recommendation and share the latest news for NVDA") and view aggregated results in a nicely formatted display. 

- **Security & Configuration:**  
  API keys and other sensitive information are stored in a `.env` file, which is excluded from version control via `.gitignore`.

## Why Use This Application?

This application empowers investors by providing quick and reliable financial insights in one place. It aggregates data from multiple sources so that investors can:
- **Make Informed Decisions:** Quickly see up-to-date analyst recommendations and news summaries, gaining insights into market sentiment.
- **Save Time:** Avoid manually searching through various sources; the tool gathers all relevant information in a single query.
- **Access Professional Data:** Benefit from information sourced from reputable financial analysts and trusted news outlets.
- **Enhance Research:** Easily digest complex financial data through clear tables and formatted text.

## Requirements

The dependencies are listed in the `requirements.txt` file. Key packages include:
- `phidata`
- `python-dotenv`
- `yfinance`
- `duckduckgo-search`
- `fastapi`
- `uvicorn`
- `groq`
- `openai`

Install all dependencies with:

```bash
pip install -r requirements.txt

```running the application
streamlit run financial_agent.py


