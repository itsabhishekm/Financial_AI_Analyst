from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv

# Loading the environment variables from .env file
load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")

#Creating the web search agent

web_search_agent=Agent(
    name="Web Search Agent",
    role="Search the web for the information",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instruction=["Always include sources"],
    show_tools_calls=True,
    markdown=True
)

## Creating a financial agent using Yfinance

finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         stock_fundamentals=True,
                         technical_indicators=True, 
                         key_financial_ratios=True),],
    description="You are an investment analyst that researches stock prices, analyst recommendations,technical_indicators,key_financial_ratios and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    #instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Now creating a multiai agent

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Always include sources","Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

#Testing this with Nvidia stock
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA",stream=True)