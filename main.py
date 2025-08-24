import asyncio
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
from tools import web_search
from decouple import config

set_tracing_disabled(True)
# 🔑 Load API key
gemini_api_key = config("GEMINI_API_KEY")

# 🌐 Initialize Gemini client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# 🔹 Agent with Tavily search tool
agent = Agent(
    name="WebSearchAgent",
    model=OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client
    ),
    tools=[web_search],
)

# ✅ Runner without args
runner = Runner()

async def main():
    print("\n🌐 Welcome to Custom Web Search Agent! (type 'exit' to quit)\n")
    while True:
        query = input("🔎 Ask me anything: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        # ✅ Await the async run call
        response = await runner.run(starting_agent=agent, input=query)
        print("\n🤖 Agent:", response.final_output, "\n")

if __name__ == "__main__":
    asyncio.run(main())
