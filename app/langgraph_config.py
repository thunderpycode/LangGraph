# import os
# from langgraph.graph import StateGraph
# from langchain_community.chat_models import ChatOpenAI  # OpenAI's native chat model
# from langchain.agents import create_openai_functions_agent, AgentExecutor
# from langchain.prompts import ChatPromptTemplate
# from langchain.tools import tool

# # Set your OpenAI API key (ensure it's set in your env)
# os.environ["OPENAI_API_KEY"] = "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"  # Replace with your real key

# @tool
# def greet(name: str) -> str:
#     """Greets a person by name."""
#     return f"Hello, {name}! How can I help you today?"

# def build_graph():
#     llm = ChatOpenAI(model="gpt-4o", temperature=0.7)  # or "gpt-3.5-turbo"

#     tools = [greet]

#     prompt = ChatPromptTemplate.from_messages([
#         ("system", "You are a helpful AI assistant."),
#         ("user", "{input}"),
#         ("ai", "{agent_scratchpad}")
#     ])

#     agent = create_openai_functions_agent(llm=llm, tools=tools, prompt=prompt)
#     executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

#     builder = StateGraph(dict)
#     builder.add_node("chat", executor)
#     builder.set_entry_point("chat")
#     builder.set_finish_point("chat")

#     return builder.compile()
import os
from langgraph.graph import StateGraph
from langchain_community.chat_models import ChatLiteLLM
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableMap

# Set OpenRouter API key and provider
os.environ["LITELLM_PROVIDER"] = "openrouter"
os.environ["OPENROUTER_API_KEY"] = "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"
os.environ["LITELLM_DEBUG"] = "True"  # Optional: Enable debug logging

def build_graph():
    llm = ChatLiteLLM(
        model="openrouter/meta-llama/llama-3-8b-instruct",
        temperature=0.7,
        max_tokens=512
    )

  
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant."),
        ("user", "{input}")
    ])

    # Chain without tool use
    chain = prompt | llm
    executor = RunnableMap({"output": chain})

    builder = StateGraph(dict)
    builder.add_node("chat", executor)
    builder.set_entry_point("chat")
    builder.set_finish_point("chat")

    return builder.compile()

