from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

# Web search agent
web_search_agent = Agent(
    name ="Web Search AI Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always show to sources"],
    show_tools_calls=True,
    markdown=True
)

#Finance agent
finance_agent = Agent(
    name="Finance AI Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display the data"],
    show_tools_calls=True,
    markdown=True
)

multi_ai_agant = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_search_agent, finance_agent],
    instructions=["Always show to sources", "Use tables to display the data"],
    show_tools_calls=True,
    markdown=True
)

# try:
#     web_search_agent.print_response("Find 10 resources on ReactJS and provide the links.", stream=True)
# except groq.APIError as e:
#     print(f"An error occurred: {e}. Please adjust your prompt and try again.")

multi_ai_agant.print_response("What is the stock price of Apple Inc. (AAPL)? also summarize the company's fundamentals and analyst recommendations.", stream=True)