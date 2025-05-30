#Note that we are hosting our agent on phidata platform for which we use the playground
#After running this file you have login to your phidata account and from there go to playground and select the end point to localhost:7777
import os
import phi
import openai
import phi.api
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq
from phi.playground import Playground, serve_playground_app

# Loading the environment variables from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

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

app=Playground(agents=[finance_agent,web_search_agent]).get_app()

if __name__=="__main__":
    #Note phidata_playground is the file name and the ":app" is pointing to where the program is going to start.
    serve_playground_app("phidata_playground:app",reload=True)

