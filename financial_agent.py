from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

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

Finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[],
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,technical_indicators=True,key_financial_ratios=True)],
    #description="You are an investment analyst that researches stock prices, analyst recommendations,technical_indicators,key_financial_ratios and stock fundamentals.",
    #instructions=["Format your response using markdown and use tables to display data where possible."],
    instructions=["Use tables to display the data"]
    show_tool_calls=True,
    markdown=True
)