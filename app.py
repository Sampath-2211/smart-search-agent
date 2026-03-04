import streamlit as st
from graph import compile_graph

# My UI Configuration
st.set_page_config(page_title="Sampath's Search Agent", page_icon="🔎")

st.title("🔎 Smart Search Researcher")
st.caption("Built by Sampath Krishna | Powered by LangGraph & Groq")

# Input Section
topic = st.text_input("Enter a topic for me to research:", placeholder="e.g., Agentic Patterns in 2026")

if st.button("Start Research"):
    if not topic:
        st.warning("I need a topic to start working!")
    else:
        # Initialize my graph
        app = compile_graph()
        
        with st.status("🤖 I am working on it...", expanded=True) as status:
            st.write("Searching the web (Tavily)...")
            result = app.invoke({"topic": topic})
            
            st.write("Summarizing with Llama 3 (Groq)...")
            status.update(label="Research Complete!", state="complete", expanded=False)
            
        st.subheader("📝 My Findings")
        st.markdown(result["final_summary"])
        
        with st.expander("View Raw Search Data"):
            st.info(result["search_data"])