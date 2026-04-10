import streamlit as st

# import your agent executor
from agent.agent import agent_executor   # or whatever your function name is
from langchain_classic.callbacks.base import BaseCallbackHandler


# ---------------------------
# Setup page
# ---------------------------
st.set_page_config(page_title="AI Agent Chat", page_icon="🤖")

st.title("🤖 ReAct AI Agent")
st.write("Chat with your intelligent tool-using agent")

# ---------------------------
# Initialize agent
# ---------------------------
@st.cache_resource
def load_agent():
    return agent_executor   # <-- your function that returns AgentExecutor

agent = load_agent()

# ---------------------------
# Session state for chat
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------
# Display chat history
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# User input
# ---------------------------
user_input = st.chat_input("Ask anything...")

if user_input:
    # show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # ---------------------------
    # Run agent
    # ---------------------------
 # ---------------------------
    # Run agent
    # ---------------------------
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = agent.invoke({
                    "input": user_input
                })

                # depending on your agent output format
                answer = response.get("output", str(response))

            except Exception as e:
                answer = f"❌ Error: {str(e)}"

        st.markdown(answer)

    # save assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})