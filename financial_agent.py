import streamlit as st
import base64
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()


with open("photos/photo3.jpg", "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()


st.markdown(
    f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: url("data:image/jpg;base64,{encoded_image}") no-repeat center center fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=OpenAIChat(engine="gpt-3.5-turbo", temperature=0.7),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance AI Agent",
    model=OpenAIChat(engine="gpt-3.5-turbo", temperature=0.7),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True
        )
    ],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display the data"],
    show_tool_calls=False,
    markdown=False,
)

st.title("Agentic AI Search Interface for Financial analysis")

query = st.text_input(
    "Enter the stock name you would like to search:",
    "Summarize analyst recommendation and share the latest news for "
)

if st.button("Search"):
    status_text = st.empty()
    status_text.write("Processing your request, please wait...")

    try:
        raw_output = multi_ai_agent.run(query)

        if hasattr(raw_output, 'content'):
            response_text = raw_output.content
        else:
            response_text = str(raw_output)

        status_text.empty()
        st.markdown(response_text)

    except Exception as e:
        status_text.empty()
        st.error(f"An error occurred: {e}")
