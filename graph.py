import os
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from tavily import TavilyClient
from dotenv import load_dotenv

# I'm loading my environment variables here
load_dotenv()

# 1. Defining the State of my Agent
class AgentState(TypedDict):
    topic: str
    search_data: str
    final_summary: str

# 2. My Search Node (Using Tavily)
def search_web(state: AgentState):
    """
    I use Tavily here because it's optimized for AI agents.
    It fetches clean context without the HTML noise.
    """
    print(f"--- I AM SEARCHING FOR: {state['topic']} ---")
    
    # Initialize the tool
    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    results = tavily.search(query=state['topic'], max_results=3)
    
    # I'm parsing the results into a single string for the LLM
    context = "\n".join([f"- {r['content']}" for r in results['results']])
    return {"search_data": context}

# 3. My Summarization Node (Using Groq)
def summarize_content(state: AgentState):
    """
    Using Groq's LPU inference here for near-instant results.
    Model: Llama 3 (70B)
    """
    print("--- I AM SUMMARIZING ---")
    
    # I chose 70B for better reasoning capabilities
    llm = ChatGroq(
        temperature=0, 
        model_name="llama3-70b-8192", 
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    prompt = f"""
    I am acting as a research assistant. 
    I need to summarize these search results about '{state['topic']}' into a clean, readable paragraph.
    
    RAW DATA:
    {state['search_data']}
    """
    
    # Invoking the chain
    response = llm.invoke(prompt)
    return {"final_summary": response.content}

# 4. Compiling my Graph
def compile_graph():
    # Defining the workflow
    workflow = StateGraph(AgentState)
    
    # Adding my nodes
    workflow.add_node("search_node", search_web)
    workflow.add_node("summarize_node", summarize_content)
    
    # Setting up the edges (the flow)
    workflow.set_entry_point("search_node")
    workflow.add_edge("search_node", "summarize_node")
    workflow.add_edge("summarize_node", END)
    
    return workflow.compile()